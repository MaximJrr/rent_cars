from datetime import date

from sqlalchemy import and_, func, insert, or_, select

from app.base_services.base import BaseService
from app.cars.models import Cars
from app.database import async_session_maker
from app.rents.models import Rents


class RentService(BaseService):
    model = Rents

    @classmethod
    async def create_new_rent(cls, car_id, user_id: int, date_from: date, date_to: date):
        async with (async_session_maker() as session):
            rented_cars = select(Rents).where(
                and_(
                    Rents.car_id == car_id,
                    or_(
                        and_(
                            Rents.date_from >= date_from,
                            Rents.date_from <= date_to
                        ),
                        and_(
                            Rents.date_from <= date_from,
                            Rents.date_to >= date_from
                        )
                    )
                )
            ).cte("rented_rooms")

            get_cars_left = select(
                (Cars.quantity - func.count(rented_cars.c.car_id)).label("cars_left")
            ).select_from(Cars).join(
                rented_cars, rented_cars.c.car_id == Cars.id, isouter=True
            ).where(Cars.id == car_id).group_by(
                Cars.id, Cars.quantity
            )

            cars_left_result = await session.execute(get_cars_left)
            cars_left = cars_left_result.scalar()

            if cars_left is None:
                cars_left = 0

            if cars_left > 0:
                get_price = select(Cars.price).filter_by(id=car_id)
                price_result = await session.execute(get_price)
                price = price_result.scalar()
                add_rent = insert(Rents).values(
                    car_id=car_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price
                ).returning(Rents)

                new_rent_result = await session.execute(add_rent)
                await session.commit()
                return new_rent_result.scalar()
            else:
                return None
