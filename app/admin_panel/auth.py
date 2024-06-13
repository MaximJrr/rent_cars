from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.exceptions import UserNotExistsException, PasswordNotCorrectException
from app.users.auth import verify_password, create_access_token
from app.users.dependencies import get_current_user
from app.users.service import UserService


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]
        user = await UserService.get_one_or_none(email=email)

        if not user:
            raise UserNotExistsException
        if user and not verify_password(password, user.hashed_password):
            raise PasswordNotCorrectException
        if user and verify_password(password, user.hashed_password):
            access_token = create_access_token({"sub": str(user.id)})
            request.session.update({"access_token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()

        return True

    async def authenticate(self, request: Request) -> RedirectResponse | bool:
        token = request.session.get("access_token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        user = await get_current_user(token)
        if not user:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        return True


authentication_backend = AdminAuth(secret_key="...")
