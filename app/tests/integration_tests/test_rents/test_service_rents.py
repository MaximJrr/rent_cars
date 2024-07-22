from app.rents.service import RentService
from datetime import datetime


async def test_rent_crud():
    new_rent = await RentService.create_new_rent(
        car_id=11,
        user_id=7,
        date_from=datetime.strptime("2025-05-05", "%Y-%m-%d"),
        date_to=datetime.strptime("2025-06-05", "%Y-%m-%d")
    )

    rent_id = await RentService.get_by_id(new_rent.id)
    deleted_rent = await RentService.delete(id=rent_id.id)

    assert new_rent.car_id == 11
    assert new_rent.user_id == 7
    assert rent_id.id is not None
    assert deleted_rent is None
