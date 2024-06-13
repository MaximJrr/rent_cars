from sqladmin import ModelView

from app.cars.models import Cars
from app.rents.models import Rents
from app.users.model import Users


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class RentsAdmin(ModelView, model=Rents):
    column_list = [c.name for c in Rents.__table__.c] + [Rents.user]
    name = "Rent"
    name_plural = "Rents"
    icon = "fa-solid fa-wallet"


class CarsAdmin(ModelView, model=Cars):
    column_list = [c.name for c in Cars.__table__.c] + [Cars.rent]
    name = "Cars"
    name_plural = "Cars"
    icon = "fa-solid fa-car"
