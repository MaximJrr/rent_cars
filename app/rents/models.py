from sqlalchemy import Column, Computed, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class Rents(Base):
    __tablename__ = "rents"
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    total_price = Column(Integer, Computed("(date_to - date_from) * price"))
    total_days = Column(Integer, Computed("date_to - date_from"))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    user_id = Column(ForeignKey("users.id"))
    car_id = Column(ForeignKey("cars.id", ondelete='CASCADE'))

    user = relationship("Users", back_populates="rent")
    car = relationship("Cars", back_populates="rent")

    def __str__(self):
        return f"Rent #{str(self.id)}"
