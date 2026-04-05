from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.services.dashboard_service import get_summary, category_totals, recent_activity
from app.utils.auth import get_current_user
from app.utils.role_checker import check_role

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/dashboard/summary")
def summary(db=Depends(get_db), user=Depends(get_current_user)):
    check_role(user["role"], ["admin", "analyst"])
    return get_summary(db)


@router.get("/dashboard/category")
def category(db=Depends(get_db), user=Depends(get_current_user)):
    check_role(user["role"], ["admin", "analyst"])
    return category_totals(db)


@router.get("/dashboard/recent")
def recent(db=Depends(get_db), user=Depends(get_current_user)):
    check_role(user["role"], ["admin", "analyst"])
    return recent_activity(db)