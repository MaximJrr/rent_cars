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
    name: str | None
    model: str | None
    price: int | None
    transmission: str | None
    wheel_drive: str | None
    quantity: int | None
    car_body: str | None
    engine: str | None
    additional_information: dict | None
    image_id: int | None

    class Config:
        orm_mode = True


class ScarsUpdate(BaseModel):
    name: str
    model: str
    price: int
    transmission: str
    wheel_drive: str
    quantity: int
    car_body: str
    engine: str
    additional_information: dict
    image_id: int

    class Config:
        orm_mode = True
