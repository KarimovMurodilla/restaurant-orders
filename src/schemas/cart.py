from pydantic import BaseModel
from typing import List, Optional

from schemas.users import UserSchema
from schemas.restaurant import RestaurantResponse
from schemas.menu_item import MenuItemResponse


class CartRequest(BaseModel):
    restaurant_id: int
    menu_item_id: int
    quantity: int

class CartResponse(BaseModel):
    id: int
    user: UserSchema
    restaurant: RestaurantResponse
    menu_item: MenuItemResponse
    quantity: int
    total_price: float

    class Config:
        from_attributes = True
