from sqlalchemy import func
from app.models import Record

def get_summary(db):
    total_income = db.query(func.sum(Record.amount))\
        .filter(Record.transaction_type == "income")\
        .scalar() or 0

    total_expense = db.query(func.sum(Record.amount))\
        .filter(Record.transaction_type == "expense")\
        .scalar() or 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    }

def category_totals(db):
    results = db.query(
        Record.category,
        func.sum(Record.amount)
    ).group_by(Record.category).all()

    return [
        {"category": r[0], "total": r[1]}
        for r in results
    ]   
    
def recent_activity(db):
    return db.query(Record)\
        .order_by(Record.date.desc())\
        .limit(5)\
        .all()