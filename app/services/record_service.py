from fastapi import HTTPException
from app.models import Record, User

def create_record(db, user_id, data):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    record = Record(
        amount=data.amount,
        transaction_type=data.transaction_type,
        category=data.category,
        date=data.date,
        description=data.description,
        user_id=user.id
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record