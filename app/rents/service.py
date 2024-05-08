from app.rents.models import Rents
from app.base_services.base import BaseService


class RentService(BaseService):
    model = Rents
