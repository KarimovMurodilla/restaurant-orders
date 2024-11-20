from pydantic import BaseModel
from typing import Optional


class EmployeeSchema(BaseModel):
    telegram_id: int
    restaurant_id: int
