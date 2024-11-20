from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.employee import EmployeeSchema

if TYPE_CHECKING:
    from db.models.cart import Cart


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column()
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


    def to_read_model(self) -> EmployeeSchema:
        return EmployeeSchema(
            telegram_id=self.telegram_id,
            restaurant_id=self.restaurant_id
        )
