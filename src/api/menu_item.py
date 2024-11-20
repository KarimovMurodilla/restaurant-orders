import io
import json
from PIL import Image
from pyzbar.pyzbar import decode

from typing import List, Optional
from fastapi import APIRouter, File, UploadFile, HTTPException, Query

from api.dependencies import UOWDep, CurrentUser

from services.menu_item import MenuService
from schemas.menu_item import MenuItemCreateRequest, MenuItemResponse


router = APIRouter(
    prefix="/menu",
    tags=["Menu"],
)

@router.post("/add-item")
async def search_menu_items(
    uow: UOWDep,
    item: MenuItemCreateRequest
):
    item_id = await MenuService().add_item(uow, item)
    return {"item_id": item_id}

@router.post("/get-menu-by-qr")
async def decode_qr_code(
    uow: UOWDep,
    file: UploadFile = File(...)
):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Iltimos rasmni faqat JPEG yoki PNG formatda yuboring")
    
    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content))
    except Exception as e:
        raise HTTPException(status_code=400, detail="Rasmni aniqlab bo'lmadi.") from e

    qr_data = decode(image)
    if not qr_data:
        raise HTTPException(status_code=400, detail="QR-kod topilmadi.")

    decoded_data = qr_data[0].data.decode("utf-8")

    try:
        data = json.loads(decoded_data)
        restaurant_id = data['restaurant_id']
    except json.decoder.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Noto'g'ri QR-kod.")

    response = await MenuService().get_menu_items_by_restaurant_id(
        uow=uow,
        restaurant_id=restaurant_id
    )
    return response

@router.get("/search", response_model=List[MenuItemResponse])
async def search_menu_items(
    uow: UOWDep,
    restaurant_id: int,
    name: str = None,
    tags: List[str] = Query(default=None, description="Teglar")
):
    return await MenuService().search_menu_items(uow, restaurant_id, name, tags)
