"""
Создание пользователя - done
Получение пользователя по id - done
Получение всех пользователей - done
Обновление пользователя по id - done
Удаление пользователя по id - done
Поиск пользователя по имени - done
"""


from fastapi import APIRouter

from api.dependencies import UOWDep

from schemas.users import UserSchemaEdit
from services.users import UsersService


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/id/{id}")
async def get_user(
    uow: UOWDep,
    id: int
):
    user = await UsersService().get_user(uow, id=id)
    return user

@router.get("/name/{name}")
async def get_user_by_name(
    uow: UOWDep,
    name: str
):
    user = await UsersService().get_user(uow, name=name)
    return user

@router.get("/all")
async def get_all_users(
    uow: UOWDep
):
    users = await UsersService().get_all_users(uow)
    return users


@router.patch("/edit/{id}")
async def edit_user(
    id: int,
    user: UserSchemaEdit,
    uow: UOWDep,
):
    await UsersService().edit_user(uow, id, user)
    return {"ok": True}


@router.delete("/delete/{id}")
async def delete_user(
    id: int,
    uow: UOWDep
):

    await UsersService().delete_user(uow, id)
    return {"ok": True}