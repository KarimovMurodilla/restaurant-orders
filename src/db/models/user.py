from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastapi_users.db import SQLAlchemyBaseUserTable

from db.db import Base

if TYPE_CHECKING:
    from db.models.cart import Cart


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[Optional[str]] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(
        String(100), 
        unique=True,
        info={"check": "email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'"}
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    carts: Mapped[List["Cart"]] = relationship(back_populates="user")
