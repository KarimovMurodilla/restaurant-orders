from db.models.users import User
from utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = User
