from fastapi import APIRouter, Depends
from datetime import date

from pydantic.tools import parse_obj_as

from app.exceptions import CarCanNotBeRentedException
from app.rents.schemas import SRents
from app.rents.service import RentService
from app.users.model import Users
from app.users.dependencies import get_current_user
from app.tasks.tasks import send_rent_confirmation_email

router = APIRouter(
    prefix="/rents",
    tags=["rents"]
)


@router.get("")
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
    await RentService.delete(id=rent_id, user_id=user.id)

