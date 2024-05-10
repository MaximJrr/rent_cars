from fastapi import APIRouter, Response, Depends

from app.exceptions import UserAlreadyExistsException, UserNotExistsException, PasswordNotCorrectException
from app.users.auth import get_hash_password, verify_password, create_access_token
from app.users.dependencies import get_current_user
from app.users.model import Users
from app.users.service import UserService
from app.users.schemas import SUsersAuth

router = APIRouter(
    prefix="/auth",
    tags=["users | auth"]
)


@router.post("/register")
async def register_user(user_data: SUsersAuth):
    existing_user = await UserService.get_one_or_none(email=user_data.email)

    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_hash_password(user_data.password)
    await UserService.create_new(email=user_data.email, hashed_password=hashed_password)

    return {"email": user_data.email}


@router.post("/login")
async def login_user(response: Response, user_data: SUsersAuth):
    user = await UserService.get_one_or_none(email=user_data.email)

    if not user:
        raise UserNotExistsException
    if user and not verify_password(user_data.password, user.hashed_password):
        raise PasswordNotCorrectException

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)

    return {"id": user.id, "access_token": access_token, "email": user.email}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")
    return {"user logout"}


@router.get("/me")
async def get_me(user: Users = Depends(get_current_user)):
    return user
