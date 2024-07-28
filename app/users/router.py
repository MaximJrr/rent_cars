from fastapi import APIRouter, Response, Depends
from fastapi.responses import JSONResponse

from app.exceptions import UserAlreadyExistsException, UserNotExistsException, PasswordNotCorrectException
from app.users.auth import get_hash_password, verify_password, create_access_token
from app.users.model import Users
from app.users.service import UserService
from app.users.schemas import SUsersAuth, SUserUpdate, SUserUpdatePartial, SUser
from app.users.dependencies import get_current_user, check_user_authorization

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
    return JSONResponse(content={"message": "user logout"})


@router.get("/me")
async def get_me(user: Users = Depends(get_current_user)):
    return user


@router.put("/{user_id}")
async def update_user(user_id: int,
                      user_update: SUserUpdate,
                      current_user: Users = Depends(check_user_authorization)
                      ) -> SUser:

    return await UserService.update(model_id=user_id, **user_update.dict())


@router.patch("/{user_id}")
async def update_user_partial(user_id: int,
                              user_update: SUserUpdatePartial,
                              current_user: Users = Depends(check_user_authorization)
                              ) -> SUser:

    return await UserService.update(model_id=user_id, **user_update.dict(exclude_unset=True))


@router.delete("/{user_id}")
async def delete_user(user_id: int, current_user: Users = Depends(check_user_authorization)):
    await UserService.delete(model_id=user_id)
    return JSONResponse(content={"message": "User deleted successfully"})
