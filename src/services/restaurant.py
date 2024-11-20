from schemas.restaurant import RestaurantCreateRequest
from utils.unitofwork import IUnitOfWork


class RestaurantService:
    async def create_restaurant(self, uow: IUnitOfWork, data: RestaurantCreateRequest):
        data_dict = data.model_dump()
        async with uow:
            order_id = await uow.restaurant.add_one(data_dict)
            await uow.commit()
            return order_id

    async def get_restaurant(self, uow: IUnitOfWork, id: int):
        async with uow:
            order = await uow.restaurant.find_one(id=id)
            return order
