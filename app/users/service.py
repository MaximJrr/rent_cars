from app.base_services.base import BaseService
from app.users.model import Users


class UserService(BaseService):
    model = Users
