from app.database import Base
from sqlalchemy import Column, Integer, String, JSON


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    car_class = Column(String, nullable=False)
    transmission = Column(String, nullable=False)
    additional_information = Column(JSON)
    image_id = Column(Integer)
