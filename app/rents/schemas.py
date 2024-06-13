from pydantic import BaseModel
from datetime import date


class SRents(BaseModel):
    id: int
    price: int
    total_price: int
    total_days: int
    date_from: date
    date_to: date
    user_id: int

    class Config:
        orm_mode = True
