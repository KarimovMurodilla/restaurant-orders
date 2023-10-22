from typing import Annotated

from fastapi import Depends

from utils.unitofwork import IUnitOfWork, UnitOfWork
from api.auth_user import current_user, User

uow = UnitOfWork
UOWDep = Annotated[IUnitOfWork, Depends(uow)]
CurrentUser = Annotated[User, Depends(current_user)]
