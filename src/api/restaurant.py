from typing import List
from fastapi import APIRouter

from api.dependencies import UOWDep, CurrentUser
from services.restaurant import RestaurantService
from schemas.restaurant import RestaurantResponse, RestaurantCreateRequest


router = APIRouter(
    prefix="/restaurant",
    tags=["Restaurant"],
)


@router.post("/")
async def create_restaurant(
    uow: UOWDep,
    restaurant_request: RestaurantCreateRequest,
):
    restaurant_id = await RestaurantService().create_restaurant(uow, restaurant_request)
    return {"restaurant_id": restaurant_id}

@router.get("/{restaurant_id}", response_model=RestaurantResponse)
async def get_restaurant(
    restaurant_id: int,
    uow: UOWDep,
):
    return await RestaurantService().get_restaurant(uow, restaurant_id)
