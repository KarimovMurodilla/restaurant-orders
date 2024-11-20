from typing import Optional
from fastapi_users.password import PasswordHelper, PasswordHelperProtocol

from schemas.users import UserSchemaAdd
from utils.unitofwork import IUnitOfWork

from db.mongodb import MongoDBManager
from utils.repository import MongoDBRepository


class UsersService:
    password_helper: PasswordHelperProtocol

    def __init__(
        self,
        password_helper: Optional[PasswordHelperProtocol] = None,
    ):
        self.mongodb = MongoDBManager.client["restaurants"]
        self.users = MongoDBRepository(self.mongodb["users"])

        if password_helper is None:
            self.password_helper = PasswordHelper()
        else:
            self.password_helper = password_helper  # pragma: no cover

    async def add_user(self, uow: IUnitOfWork, user: UserSchemaAdd):
        user_dict = user.model_dump()
        async with uow:
            await uow.users.add_one(user_dict)
            await self.users.add_one(user_dict)
            await uow.commit()
        
    async def get_user(self, uow: IUnitOfWork, **filters: dict):
        async with uow:
            # user = await uow.users.find_one(**filters)
            user = await self.users.find_one(**filters)
            return user

    async def get_all_users(self, uow: IUnitOfWork):
        async with uow:
            # users = await uow.users.find_all()
            users = await self.users.find_all()
            return users

    async def filter_users(self, uow: IUnitOfWork, **filters: dict):
        async with uow:
            # users = await uow.users.find_all_by(**filters)
            users = await self.users.find_all_by(**filters)
            return users
