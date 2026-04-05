from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.schemas import UserCreate
from app.services.user_service import create_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users")
def create(data: UserCreate, db=Depends(get_db)):
    return create_user(db, data)