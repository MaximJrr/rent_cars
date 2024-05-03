from app.database import Base
from sqlalchemy import Column, String, Integer


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String)
    passport_id = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
