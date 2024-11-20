from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from schemas.cart import CartResponse

if TYPE_CHECKING:
    from db.models.user import User
    from db.models.restaurant import Restaurant
    from db.models.menu_item import MenuItem


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id", ondelete="CASCADE"))
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("menu_items.id", ondelete="CASCADE"))
    quantity: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint('menu_item_id', 'restaurant_id', name='uq_user_restaurant_cart'),
    )

    user: Mapped["User"] = relationship(back_populates="carts", lazy="joined")
    restaurant: Mapped["Restaurant"] = relationship(back_populates="carts", lazy="joined")
    menu_item: Mapped["MenuItem"] = relationship(lazy="joined")

    def to_read_model(self) -> CartResponse:
        return CartResponse(
            id=self.id,
            user=self.user,
            restaurant=self.restaurant,
            menu_item=self.menu_item,
            quantity=self.quantity,
            total_price=self.quantity * self.menu_item.price
        )
