from fastapi import HTTPException
from app.models import User

def create_user(db, data):
    existing = db.query(User).filter(User.email == data.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    user = User(**data.dict())

    db.add(user)
    db.commit()
    db.refresh(user)

    return user