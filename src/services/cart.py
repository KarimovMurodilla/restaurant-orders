import aiohttp
from typing import List

from utils.unitofwork import IUnitOfWork
from schemas.cart import CartRequest, CartResponse
from schemas.employee import EmployeeSchema
from config import BOT_TOKEN

from db.mongodb import MongoDBManager
from utils.repository import MongoDBRepository


class CartService:
    def __init__(self):
        self.mongodb = MongoDBManager.client["restaurants"]
        self.cart = MongoDBRepository(self.mongodb["cart"])
        
    async def send_message(token, chat_id, text): 
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage' 
        payload = { 'chat_id': chat_id, 'text': text }
        try:
            async with aiohttp.ClientSession() as session: 
                async with session.post(url, json=payload) as response: 
                    if response.status == 200: 
                        print("Habar muvaffaqiyatli jo'natildi!")
                    else:
                        print("Habarni yuborishda hatolik yuz berdi")
        except:
            print("Habarni yuborishda qandaydir hatolik yuz berdi")
        
    async def add_to_cart(self, uow: IUnitOfWork, user_id: int, item: CartRequest):
        item_dict = item.model_dump()
        item_dict['user_id'] = user_id
        async with uow:
            item_id = await uow.cart.add_one(item_dict)
            await uow.commit()

            await self.cart.add_one(item_dict)
            return item_id

    async def get_cart(self, uow: IUnitOfWork, user_id: int):
        async with uow:
            cart_items = await uow.cart.find_all_by(user_id=user_id)
            return cart_items

    async def remove_from_cart(self, uow: IUnitOfWork, id: int):
        async with uow:
            await uow.cart.delete_one(id=id)
            await self.cart.delete_one(id=id)
            await uow.commit()

    async def send_order_to_employees(self, uow: IUnitOfWork, items: List[CartResponse]):
        text = ""
        text += f"Restoran nomi: {items[0].restaurant.name}\n\n"
        text += f"Mijozning ismi: {items[0].user.name}\n"
        text += f"Mijozning telefon raqami: {items[0].user.phone_number}\n\n"
        
        text += "Buyurtmalar:\n"
        total = 0
        for item in items:
            text += f"{item.menu_item.name} - {item.menu_item.price} so'm\n"
            total += item.menu_item.price
        
        text += f"Umumiy summa: {total}"

        async with uow:
            restaurant_id = items[0].restaurant.id
            employees: List[EmployeeSchema] = await uow.employee.find_all_by(restaurant_id=restaurant_id)

            if not employees:
                return False
            
            for employee in employees:
                await self.send_message(employee.telegram_id, text)
        
            for item in items:
                await uow.cart.delete_one(id=item.id)

            await uow.commit()

        return True

        
