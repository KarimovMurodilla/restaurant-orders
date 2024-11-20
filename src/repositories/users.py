from db.models.user import User
from utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = User
