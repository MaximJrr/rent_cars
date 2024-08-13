from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (
    ExpiredTokenException,
    InvalidTokenFormatException,
    NotAuthorizedToUpdateThisUser,
    TokenNotExistsException,
    UserNotExistsException,
    UserNotFoundException,
)
from app.users.model import Users
from app.users.service import UserService


def get_token(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        raise TokenNotExistsException

    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise InvalidTokenFormatException

    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise ExpiredTokenException

    user_id: str = payload.get("sub")
    if not user_id:
        raise UserNotExistsException

    user = await UserService.get_by_id(int(user_id))
    if not user:
        raise UserNotExistsException

    return user


async def check_user_authorization(user_id: int, current_user: Users = Depends(get_current_user)):
    user = await UserService.get_by_id(model_id=user_id)

    if user_id != current_user.id:
        raise NotAuthorizedToUpdateThisUser

    if not user:
        raise UserNotFoundException

    return current_user
