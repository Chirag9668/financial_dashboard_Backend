from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    is_active: bool = True


class RecordCreate(BaseModel):
    amount: float
    transaction_type: str
    category: str
    date: date
    description: Optional[str] = None


class RecordResponse(BaseModel):
    amount: float
    transaction_type: str
    category: str
    date: date
    description: Optional[str]

    class Config:
        from_attributes = True