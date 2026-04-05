from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String)
    is_active = Column(Boolean, default=True)


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    transaction_type = Column(String)
    category = Column(String)
    date = Column(Date)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))