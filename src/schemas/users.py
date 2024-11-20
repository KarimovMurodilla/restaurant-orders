import datetime
from typing import List, Optional

from fastapi_users import schemas

from pydantic import BaseModel, EmailStr


class UserSchema(schemas.BaseUser[int]):
    id: int
    name: str
    phone_number: str
    email: str

    class ConfigDict:
        from_attributes = True

class UserSchemaAdd(schemas.BaseUserCreate):
    name: str
    phone_number: Optional[str] = None
    email: EmailStr
