from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from schemas.restaurant import RestaurantResponse

from db.db import Base

if TYPE_CHECKING:
    from db.models.menu_item import MenuItem
    from db.models.cart import Cart

class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    menu_items: Mapped[List["MenuItem"]] = relationship(back_populates="restaurant")
    carts: Mapped[List["Cart"]] = relationship(back_populates="restaurant")

    def to_read_model(self) -> RestaurantResponse:
        return RestaurantResponse(
            id=self.id,
            name=self.name,
            created_at=self.created_at
        )
