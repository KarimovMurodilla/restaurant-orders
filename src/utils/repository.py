from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select
from sqlalchemy.sql import or_, any_
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()

    async def edit_one(self, id: int, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()
    
    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    async def find_all_by(self, **filters: dict):
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    async def find_one(self, **filters: dict):
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.execute(stmt)
        res = res.scalar_one_or_none()

        if res:
            res = res.to_read_model()
            
        return res

    async def delete_one(self, **filters: dict) -> int:
        stmt = delete(self.model).filter_by(**filters).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()

    async def search_menu_items(
        self,
        restaurant_id: int,
        query: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ):
        stmt = select(self.model).filter_by(restaurant_id=restaurant_id)

        if query:
            stmt = stmt.where(self.model.name.ilike(f"%{query}%"))

        if tags:
            stmt = stmt.where(
                or_(*[tag == any_(self.model.tags) for tag in tags])
            )

        result = await self.session.execute(stmt)
        menu_items = result.scalars().all()

        return menu_items
