from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Computed


class Rents(Base):
    __tablename__ = "rents"
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    total_price = Column(Integer, Computed("(date_to - date_from) * price"))
    total_days = Column(Integer, Computed("date_from - date_to"))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    user_id = Column(ForeignKey('users.id'))

