from typing import Optional, List

from schemas.menu_item import MenuItemCreateRequest, MenuItemResponse
from utils.unitofwork import IUnitOfWork

from db.mongodb import MongoDBManager
from utils.repository import MongoDBRepository


class MenuService:
    def __init__(self):
        self.mongodb = MongoDBManager.client["restaurants"]
        self.menu_items = MongoDBRepository(self.mongodb["menu_items"])

    async def add_item(self, uow: IUnitOfWork, item: MenuItemCreateRequest):
        item_dict = item.model_dump()
        async with uow:
            item_id = await uow.menu_item.add_one(item_dict) # PostgreSQL
            await self.menu_items.add_one(item_dict) # MongoDB
            await uow.commit()
            return item_id

    async def get_menu_items_by_restaurant_id(self, uow: IUnitOfWork, restaurant_id: int):
        # async with uow:
            # menu_items = await uow.menu_item.find_all_by(restaurant_id=restaurant_id)
        menu_items = await self.menu_items.find_all_by(restaurant_id=restaurant_id)
        return menu_items

    async def search_menu_items(
        self,
        uow: IUnitOfWork,
        restaurant_id: int,
        query: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> List[MenuItemResponse]:
        # async with uow:
            # menu_items = await uow.menu_item.search_menu_items(restaurant_id, query, tags)
        menu_items = await self.menu_items.search_menu_items(restaurant_id, query, tags)
        return [MenuItemResponse.model_validate(item) for item in menu_items]
