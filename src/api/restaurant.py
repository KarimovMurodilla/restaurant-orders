import qrcode

from fastapi import APIRouter

from api.dependencies import UOWDep
from services.restaurant import RestaurantService
from schemas.restaurant import RestaurantCreateRequest

from config import BASE_DIR


router = APIRouter(
    prefix="/restaurant",
    tags=["Restaurant"],
)

def generate_qr(restaurant_id):
    data = {"restaurant_id": restaurant_id}

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    image_path = BASE_DIR / f"src/static/qr/restaurant_{restaurant_id}.png"
    img.save(image_path)
    return image_path


@router.post("/")
async def create_restaurant(
    uow: UOWDep,
    restaurant_request: RestaurantCreateRequest,
):
    restaurant_id = await RestaurantService().create_restaurant(uow, restaurant_request)
    qr_code = generate_qr(restaurant_id)
    return {"restaurant_id": restaurant_id, "qr_code": qr_code}

@router.get("/{restaurant_id}")
async def get_restaurant(
    restaurant_id: int,
    uow: UOWDep,
):
    return await RestaurantService().get_restaurant(uow, restaurant_id)
