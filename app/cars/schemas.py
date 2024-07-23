from typing import Optional
from pydantic import BaseModel


class CarArgs:
    def __init__(
        self,
        car_id: int,
        name: Optional[str] = None,
        model: Optional[str] = None,
        price: Optional[str] = None,
        car_body: Optional[str] = None,
        transmission: Optional[str] = None,
        engine: Optional[str] = None,
        wheel_drive: Optional[str] = None
    ):
        self.car_id = car_id
        self.name = name
        self.model = model
        self.price = price
        self.car_body = car_body
        self.transmission = transmission
        self.engine = engine
        self.wheel_drive = wheel_drive


class SCars(BaseModel):
    id: int
    name: str
    model: Optional[str] = None
    price: Optional[int] = None
    transmission: Optional[str] = None
    wheel_drive: Optional[str] = None
    quantity: Optional[int] = None
    car_body: Optional[str] = None
    engine: Optional[str] = None
    additional_information: Optional[dict] = None
    image_id: Optional[int] = None

    class Config:
        orm_mode = True
