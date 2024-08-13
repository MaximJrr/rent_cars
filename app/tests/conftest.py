import asyncio
import json
from datetime import datetime

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import insert

from app.cars.models import Cars
from app.config import settings
from app.database import Base, async_session_maker, engine
from app.main import app as fastapi_app
from app.rents.models import Rents
from app.users.model import Users


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_json(model: str):
        with open(f"app/tests/mock_{model}.json", "r") as file:
            return json.load(file)

    users = open_json("users")
    cars = open_json("cars")
    rents = open_json("rents")

    for rent in rents:
        rent["date_from"] = datetime.strptime(rent["date_from"], "%Y-%m-%d")
        rent["date_to"] = datetime.strptime(rent["date_to"], "%Y-%m-%d")

    async with async_session_maker() as session:
        add_users = insert(Users).values(users)
        add_cars = insert(Cars).values(cars)
        add_rents = insert(Rents).values(rents)

        await session.execute(add_users)
        await session.execute(add_cars)
        await session.execute(add_rents)

        await session.commit()


@pytest_asyncio.fixture(scope='session', autouse=True)
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def async_client():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="session")
async def authenticated_async_client():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as client:
        await client.post("/auth/login", json={
            "email": "user@example.com",
            "password": "string"
        })
        assert client.cookies["access_token"]
        yield client
