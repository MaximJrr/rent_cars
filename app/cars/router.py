from fastapi import APIRouter
from app.cars.service import CarService
from fastapi_cache.decorator import cache

from app.exceptions import NoCarsException

router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)


@router.get("/{name}")
# @cache(expire=30)
async def get_cars(name: str):
    cars = await CarService.get_all(name=name)

    if not cars:
        raise NoCarsException

    return cars
