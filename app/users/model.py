from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    passport_id = Column(String)
    phone_number = Column(String)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    rent = relationship("Rents", back_populates="user")

    def __str__(self):
        return f"Name: {self.name}, Last name: {self.last_name}, Email: {self.email}"
