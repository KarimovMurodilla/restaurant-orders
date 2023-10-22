import datetime
from typing import List, Optional

from fastapi_users import schemas

from pydantic import BaseModel


class UserSchema(schemas.BaseUser[int]):
    id: int
    name: str
    email: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class ConfigDict:
        from_attributes = True


class UserSchemaAdd(schemas.BaseUserCreate):
    name: str


class UserSchemaEdit(schemas.BaseUserUpdate):
    name: str