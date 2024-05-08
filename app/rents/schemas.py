from pydantic import BaseModel


class SRents(BaseModel):
    id: int
    price: int
    total_price: int
    total_days: int
    date_from: int
    date_to: int
    user_id: int

    class Config:
        orm_mode = True
