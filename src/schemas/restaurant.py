from pydantic import BaseModel
from typing import Optional, List

from schemas.menu_item import MenuItemResponse


class RestaurantCreateRequest(BaseModel):
    name: str

class RestaurantResponse(BaseModel):
    id: int
    name: str
    # menu_items: List[MenuItemResponse]

    class Config:
        from_attributes = True
