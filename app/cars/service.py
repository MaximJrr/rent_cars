from sqlalchemy import select

from app.base_services.base import BaseService
from app.cars.models import Cars
from app.database import async_session_maker


class CarService(BaseService):
    model = Cars

    @classmethod
    async def get_available_cars(cls):
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.quantity > 1)
            result = await session.execute(query)
            return result.scalars().all()
