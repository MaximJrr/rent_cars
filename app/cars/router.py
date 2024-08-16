from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
from pydantic.tools import parse_obj_as

from app.cars.schemas import SCars, SCarsCreate, ScarsUpdate
from app.cars.service import CarService
from app.exceptions import NoCarException
from app.tasks.tasks import send_new_car_message_email
from app.users.service import UserService

router = APIRouter(
    prefix="/api/cars",
    tags=["cars"]
)


@router.get("")
@cache(expire=30)
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


@router.get("/available/")
@cache(expire=30)
async def get_available_cars() -> list[SCars]:
    return await CarService.get_available_cars()


@router.post("")
async def create_new_car(cars: SCarsCreate):
    new_car = await CarService.create_new(**cars.dict())
    users = await UserService.get_all()
    emails = []

    for email in users:
        emails.append(email.email)

    car_dict = parse_obj_as(SCars, new_car).dict()
    send_new_car_message_email.delay(car_dict, emails)

    return JSONResponse(content={"message": "the car successfully created"})
