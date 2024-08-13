from datetime import date

from pydantic import BaseModel


class SRents(BaseModel):
    id: int
    price: int
    total_price: int
    total_days: int
    date_from: date
    date_to: date
    car_id: int

    class Config:
        orm_mode = True
