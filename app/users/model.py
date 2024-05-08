from app.database import Base
from sqlalchemy import Column, String, Integer


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    passport_id = Column(String)
    phone_number = Column(String)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
