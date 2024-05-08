from app.users.model import Users
from app.base_services.base import BaseService


class UserService(BaseService):
    model = Users
