from fastapi import APIRouter, Depends
from app.rents.service import RentService
from app.users.model import Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/rents",
    tags=["rents"]
)


@router.get("")
async def get_rents(user: Users = Depends(get_current_user)):
    return await RentService.get_all(user_id=user.id)
