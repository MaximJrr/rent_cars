import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.parametrize("email, password, status_code", [
    ("test_user@gmail.com", "test_password1234", status.HTTP_200_OK),
    ("test_user@gmail.com", 'test_password12345', status.HTTP_409_CONFLICT),
    ("test", "test", status.HTTP_422_UNPROCESSABLE_ENTITY)
])
async def test_register_user(email, password, status_code, async_client: AsyncClient):
    response = await async_client.post("/auth/register", json={
        "email": email,
        "password": password
    })

    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("user@example.com", "string", status.HTTP_200_OK),
    ("user1@example.com", "string", status.HTTP_401_UNAUTHORIZED),
    ("user@example.com", "string1", status.HTTP_401_UNAUTHORIZED)
])
async def test_login_user(email, password, status_code, async_client: AsyncClient):
    response = await async_client.post("/auth/login", json={
        "email": email,
        "password": password
    })

    assert response.status_code == status_code


async def test_get_me(authenticated_async_client: AsyncClient):
    request = await authenticated_async_client.get("/auth/me")

    assert request.status_code == 200


async def test_logout_user(authenticated_async_client: AsyncClient):
    cookie = authenticated_async_client.cookies

    assert cookie is not None

    response = await authenticated_async_client.post("/auth/logout")
    cookie = response.cookies

    assert cookie is not None
    assert cookie is not None
    assert response.status_code == 200
