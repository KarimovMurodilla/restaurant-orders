from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from sqlalchemy.future import select
from sqlalchemy.sql import or_, any_
# from sqlalchemy.dialects.postgresql import any_

from schemas.menu_item import MenuItemCreateRequest, MenuItemResponse
from utils.unitofwork import IUnitOfWork


class MenuService:
    async def add_item(self, uow: IUnitOfWork, item: MenuItemCreateRequest):
        item_dict = item.model_dump()
        async with uow:
            item_id = await uow.menu_item.add_one(item_dict)
            await uow.commit()
            return item_id

    async def get_menu_items_by_restaurant_id(self, uow: IUnitOfWork, restaurant_id: int):
        async with uow:
            menu_items = await uow.menu_item.find_all_by(restaurant_id=restaurant_id)
            return menu_items

    async def search_menu_items(
        self,
        uow: IUnitOfWork,
        restaurant_id: int,
        query: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> List[MenuItemResponse]:
        async with uow:
            menu_items = await uow.menu_item.search_menu_items(restaurant_id, query, tags)
            return [MenuItemResponse.model_validate(item) for item in menu_items]
