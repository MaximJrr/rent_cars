from fastapi import APIRouter
from app.cars.schemas import SCars, ScarsUpdate
from app.cars.service import CarService
from app.exceptions import NoCarException


router = APIRouter(
    prefix="/api/cars",
    tags=["cars"]
)


@router.get("")
async def get_all_cars() -> list[SCars]:
    return await CarService.get_all()


@router.get("/{car_id}")
async def get_car_by_id(car_id: int) -> SCars:
    car = await CarService.get_by_id(model_id=car_id)

    if not car:
        raise NoCarException

    return car


@router.put("/{car_id}")
async def update_car(car_id: int, car_update: ScarsUpdate) -> SCars:
    car = await CarService.get_by_id(model_id=car_id)

    if not car:
        raise NoCarException

    return await CarService.update(model_id=car_id, **car_update.dict())


@router.delete("/{car_id}")
async def delete_car(car_id: int):
    return await CarService.delete(model_id=car_id)
