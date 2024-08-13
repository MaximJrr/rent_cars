from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


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

    rent = relationship("Rents", back_populates="car", cascade="all, delete-orphan")

    def __str__(self):
        return f"Car name: {self.name}, price: {self.price}"
