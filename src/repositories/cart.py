from db.models.cart import Cart
from utils.repository import SQLAlchemyRepository


class CartRepository(SQLAlchemyRepository):
    model = Cart
