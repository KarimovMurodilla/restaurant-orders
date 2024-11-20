from fastapi import APIRouter

from api.dependencies import UOWDep

from services.users import UsersService


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# @router.get("/user_id/{id}")
# async def get_user(
#     uow: UOWDep,
#     id: int
# ):
#     user = await UsersService().get_user(uow, id=id)
#     return user
