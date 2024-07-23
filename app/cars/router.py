from fastapi import APIRouter
from fastapi import Depends
from app.cars.schemas import CarArgs, SCars
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
async def update_car(car_args: CarArgs = Depends()):
    return await CarService.update(model_id=car_args.car_id,
                                   name=car_args.name,
                                   model=car_args.model,
                                   price=car_args.price,
                                   car_body=car_args.car_body,
                                   transmission=car_args.transmission,
                                   engine=car_args.engine,
                                   wheel_drive=car_args.wheel_drive
                                   )


@router.delete("/{car_id}")
async def delete_car(car_id: int):
    return await CarService.delete(model_id=car_id)
