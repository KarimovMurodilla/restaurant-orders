from schemas.restaurant import RestaurantCreateRequest
from utils.unitofwork import IUnitOfWork

from db.mongodb import MongoDBManager
from utils.repository import MongoDBRepository

class RestaurantService:
    def __init__(self):
        self.mongodb = MongoDBManager.client["restaurants"]
        self.restaurants = MongoDBRepository(self.mongodb["restaurants"])

    async def create_restaurant(self, uow: IUnitOfWork, data: RestaurantCreateRequest):
        data_dict = data.model_dump()
        async with uow:
            restaurant_id = await uow.restaurant.add_one(data_dict)
            data_dict['restaurant_id'] = restaurant_id
            await self.restaurants.add_one(data_dict)
            await uow.commit()
            return restaurant_id

    async def get_restaurant(self, uow: IUnitOfWork, id: int):
        async with uow:
            # restaurant = await uow.restaurant.find_one(id=id)
            restaurant = await self.restaurants.find_one(restaurant_id=id)
            return restaurant
