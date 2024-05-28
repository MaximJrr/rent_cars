from fastapi import APIRouter, Depends
from datetime import date

from app.exceptions import CarCanNotBeRented
from app.rents.schemas import SRents
from app.rents.service import RentService
from app.users.model import Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/rents",
    tags=["rents"]
)


@router.get("")
async def get_rents(user: Users = Depends(get_current_user)) -> list[SRents]:
    return await RentService.get_all(user_id=user.id)


@router.post("")
async def test_get_rents(car_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    rents = await RentService.create_new_rent(car_id, user.id, date_from, date_to)
    if not rents:
        raise CarCanNotBeRented
    return rents
