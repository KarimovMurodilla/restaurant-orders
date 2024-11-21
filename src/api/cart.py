from typing import Optional
from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError
from asyncpg.exceptions import ForeignKeyViolationError

from api.dependencies import UOWDep, CurrentUser

from services.cart import CartService
from schemas.cart import CartResponse, CartRequest


router = APIRouter(
    prefix="/cart",
    tags=["Cart"],
)


@router.post("")
async def add_to_cart(
    uow: UOWDep,
    cart_request: CartRequest,
    user: CurrentUser
):
    if cart_request.quantity == 0:
        return {"message": "Kamida bitta ovqat oling)"}
    try:
        item_id = await CartService().add_to_cart(uow, user.id, cart_request)
        return {"item_id": item_id}
    except IntegrityError as e:
        if isinstance(e.orig, ForeignKeyViolationError): 
            return {"message": "Bunday ovqat mavjud emas"}
        return {"message": "Ushbu ovqat savatda mavjud"}
    
@router.post("/make-order")
async def make_order(
    uow: UOWDep,
    user: CurrentUser
):
    """
    Savatdagi ovqatlarni buyurtma qilish
    """

    items = await CartService().get_cart(uow, user.id)
    if not items:
        return {"message": "Savatingizda hech narsa yo'q("}
    
    result = await CartService().send_order_to_employees(uow, items)

    if result:
        return {"message": "Buyurtmangiz jo'natildi"}
    else:
        return {"message": "Restoran hodimlari topilmadi"}

@router.get("")
async def get_cart(
    uow: UOWDep,
    user: CurrentUser
):
    cart_items = await CartService().get_cart(uow, user.id)
    return cart_items

@router.delete("/{item_id}")
async def remove_from_cart(
    item_id: int,
    uow: UOWDep,
    user: CurrentUser
):
    await CartService().remove_from_cart(uow, item_id)
