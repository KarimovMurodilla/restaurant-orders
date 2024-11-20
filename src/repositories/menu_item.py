from db.models.menu_item import MenuItem
from utils.repository import SQLAlchemyRepository


class MenuItemRepository(SQLAlchemyRepository):
    model = MenuItem
