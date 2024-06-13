from fastapi import APIRouter
from app.cars.service import CarService
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)


@router.get("/{name}")
@cache(expire=30)
async def get_cars(name: str):
    return await CarService.get_all(name=name)
