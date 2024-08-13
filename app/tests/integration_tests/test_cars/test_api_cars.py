import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.parametrize("name, status_code", [
    ("BMW", status.HTTP_200_OK),
    ("error", status.HTTP_409_CONFLICT)
])
async def test_get_cars(name, status_code, async_client: AsyncClient):
    request = await async_client.get(f"/cars/{name}")

    assert request.status_code == status_code
