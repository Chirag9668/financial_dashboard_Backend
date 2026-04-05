from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.schemas import RecordCreate, RecordResponse
from app.services.record_service import create_record
from app.models import Record
from app.utils.auth import get_current_user
from app.utils.role_checker import check_role

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/records", response_model=RecordResponse)
def create(data: RecordCreate, db=Depends(get_db), user=Depends(get_current_user)):
    check_role(user["role"], ["admin"])
    return create_record(db, user["id"], data)


@router.post("/records/batch", response_model=list[RecordResponse])
def batch_create(records: list[RecordCreate], db=Depends(get_db), user=Depends(get_current_user)):
    check_role(user["role"], ["admin"])

    created = []
    for r in records:
        created.append(create_record(db, user["id"], r))

    return created


@router.get("/records")
def get_all(db=Depends(get_db)):
    return db.query(Record).all()


@router.delete("/records/{id}")
def delete(id: int, db=Depends(get_db), user=Depends(get_current_user)):
    check_role(user["role"], ["admin"])

    record = db.query(Record).filter(Record.id == id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(record)
    db.commit()

    return {"message": "Deleted"}