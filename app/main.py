from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.admin_panel.auth import authentication_backend
from app.admin_panel.views import UsersAdmin, RentsAdmin, CarsAdmin
from app.database import engine
from app.rents.router import router as router_rents
from app.cars.router import router as router_cars
from app.users.router import router as router_users
from app.pages.router import router as router_pages
from app.images.router import router as router_images
from app.config import settings

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from sqladmin import Admin

from redis import asyncio as aioredis

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_rents)
app.include_router(router_cars)
app.include_router(router_users)

app.include_router(router_pages)
app.include_router(router_images)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)
admin.add_view(RentsAdmin)
admin.add_view(CarsAdmin)


@app.on_event("startup")
def startup():
    redis = aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8", decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="cache")
