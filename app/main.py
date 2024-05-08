from fastapi import FastAPI
from app.rents.router import router as router_rents
from app.cars.router import router as router_cars
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_rents)
app.include_router(router_cars)
app.include_router(router_users)
