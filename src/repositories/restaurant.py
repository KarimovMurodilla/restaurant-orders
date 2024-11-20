from db.models.restaurant import Restaurant
from utils.repository import SQLAlchemyRepository


class RestaurantRepository(SQLAlchemyRepository):
    model = Restaurant
