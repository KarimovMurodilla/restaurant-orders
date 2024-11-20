from pydantic import BaseModel
from typing import Optional, Union


class MenuItemCreateRequest(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tags: Optional[list[str]]
    restaurant_id: int

class MenuItemResponse(BaseModel):
    id: Union[int, str]
    name: str
    description: Optional[str]
    price: float
    tags: Optional[list[str]]

    class Config:
        from_attributes = True
