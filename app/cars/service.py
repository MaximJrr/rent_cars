from app.cars.models import Cars
from app.base_services.base import BaseService


class CarService(BaseService):
    model = Cars
