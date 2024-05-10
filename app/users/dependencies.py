from datetime import datetime
from fastapi import Request, Depends
from jose import jwt, JWTError
from app.config import settings
from app.exceptions import TokenNotExistsException, InvalidTokenFormatException, ExpiredTokenException, \
    UserNotExistsException
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
