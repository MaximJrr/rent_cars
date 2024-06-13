from app.database import Base
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship


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

    rent = relationship("Rents", back_populates="car")

    def __str__(self):
        return f"Car name: {self.name}, price: {self.price}"
