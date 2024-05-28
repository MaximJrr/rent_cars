from app.database import Base
from sqlalchemy import Column, Integer, String, JSON


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String)
    price = Column(Integer)
    car_body = Column(String)
    transmission = Column(String)
    engine = Column(String)
    wheel_drive = Column(String)
    additional_information = Column(JSON)
    quantity = Column(Integer)
    image_id = Column(Integer)
