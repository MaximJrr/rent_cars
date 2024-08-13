from datetime import date

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from pydantic.tools import parse_obj_as

from app.exceptions import CarCanNotBeRentedException, NoRentException
from app.rents.schemas import SRents
from app.rents.service import RentService
from app.tasks.tasks import send_rent_confirmation_email
from app.users.dependencies import get_current_user
from app.users.model import Users

router = APIRouter(
    prefix="/rents",
    tags=["rents"]
)


@router.get("")
@cache(expire=30)
async def get_rents(user: Users = Depends(get_current_user)) -> list[SRents]:
    return await RentService.get_all(user_id=user.id)


@router.post("")
async def create_rent(car_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    rent = await RentService.create_new_rent(car_id, user.id, date_from, date_to)

    if not rent:
        raise CarCanNotBeRentedException

    rent_dict = parse_obj_as(SRents, rent).dict()
    send_rent_confirmation_email.delay(rent_dict, user.email)
    return rent_dict


@router.delete("/{rent_id}")
async def delete_rent(rent_id: int, user: Users = Depends(get_current_user)):
    await RentService.delete(model_id=rent_id)


@router.get("/{rent_id}")
async def get_rent_by_id(rent_id: int, user: Users = Depends(get_current_user)) -> SRents:
    rent = await RentService.get_by_id(model_id=rent_id)

    if not rent:
        raise NoRentException

    return rent
