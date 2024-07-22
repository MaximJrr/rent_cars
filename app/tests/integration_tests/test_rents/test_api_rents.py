from httpx import AsyncClient
import pytest
from fastapi import status


@pytest.mark.parametrize("car_id, date_from, date_to, status_code", [
    (10, "2024-05-05", "2025-05-15", status.HTTP_200_OK),
    (10, "2024-05-05", "2025-05-15", status.HTTP_200_OK),
    (10, "2024-05-05", "2025-05-15", status.HTTP_409_CONFLICT),

])
async def test_create_new_rent_and_get_rent(car_id, date_from, date_to,
                                            status_code, authenticated_async_client: AsyncClient):
    request = await authenticated_async_client.post("/rents", params={
        "car_id": car_id,
        "date_from": date_from,
        "date_to": date_to
    })

    assert request.status_code == status_code


async def test_get_rents_and_delete_rents(authenticated_async_client: AsyncClient):
    request = await authenticated_async_client.get("/rents")
    rents = [r['id'] for r in request.json()]

    for r in rents:
        await authenticated_async_client.delete(f'/rents/{r}')

    request = await authenticated_async_client.get("/rents")

    assert len(request.json()) == 0


@pytest.mark.parametrize("rent_id, status_code", [
    (1, status.HTTP_200_OK),
    (2, status.HTTP_200_OK)
])
async def test_delete_rents(rent_id, status_code, authenticated_async_client: AsyncClient):
    request = await authenticated_async_client.delete(f"rents/{rent_id}")

    assert request.status_code == 200
    assert request.status_code == 200
