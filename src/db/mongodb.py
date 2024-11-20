from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import IndexModel, ASCENDING
from typing import Optional

class MongoDBManager:
    client: Optional[AsyncIOMotorClient] = None
    
    @classmethod
    async def connect_to_mongodb(cls, mongodb_url: str, db_name: str):
        cls.client = AsyncIOMotorClient(mongodb_url)
        db = cls.client[db_name]
        
        users = db.users
        await users.create_indexes([
            IndexModel([("email", ASCENDING)], unique=True),
            IndexModel([("phone_number", ASCENDING)])
        ])

        restaurants = db.restaurants
        await restaurants.create_indexes([
            IndexModel([("name", ASCENDING)]),  # Индекс для поиска по названию ресторана
            IndexModel([("location", ASCENDING)])  # Если используется местоположение ресторана
        ])

        menu_items = db.menu_items
        await menu_items.create_indexes([
            IndexModel([("restaurant_id", ASCENDING)]),
            IndexModel([("name", ASCENDING)]),
            IndexModel([("tags", ASCENDING)]),
            IndexModel([("price", ASCENDING)])
        ])

        carts = db.carts
        await carts.create_indexes([
            IndexModel([("user_id", ASCENDING)]),  # Для поиска корзины пользователя
            IndexModel([("restaurant_id", ASCENDING)]),  # Для поиска корзины по ресторану
            IndexModel([("menu_item_id", ASCENDING)])  # Для работы с элементами меню в корзине
        ])

        return cls.client
    
    @classmethod
    async def close_mongodb_connection(cls):
        if cls.client is not None:
            cls.client.close()
