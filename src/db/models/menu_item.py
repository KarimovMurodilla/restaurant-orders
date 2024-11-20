from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from decimal import Decimal

from sqlalchemy import ForeignKey, String, Numeric, Text, Boolean, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY

from db.db import Base
from schemas.menu_item import MenuItemResponse

if TYPE_CHECKING:
    from db.models.restaurant import Restaurant


class MenuItem(Base):
    __tablename__ = "menu_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(Text)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    tags: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String))
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    image_url: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint('price >= 0', name='check_positive_price'),
    )

    restaurant: Mapped["Restaurant"] = relationship(back_populates="menu_items")

    def to_read_model(self) -> MenuItemResponse:
        return MenuItemResponse(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price,
            tags=self.tags,
            created_at=self.created_at
        )
