from models.record import Record
from database.db import db
from sqlalchemy import func


def get_summary():
    total_income = db.session.query(func.sum(Record.amount)).filter(Record.type == "income").scalar() or 0
    total_expense = db.session.query(func.sum(Record.amount)).filter(Record.type == "expense").scalar() or 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }, 200


def category_wise():
    data = db.session.query(
        Record.category,
        func.sum(Record.amount)
    ).group_by(Record.category).all()

    result = []
    for category, total in data:
        result.append({
            "category": category,
            "total": total
        })

    return result, 200


def recent_transactions():
    records = Record.query.order_by(Record.id.desc()).limit(5).all()

    result = []
    for r in records:
        result.append({
            "id": r.id,
            "amount": r.amount,
            "type": r.type,
            "category": r.category,
            "date": r.date
        })

    return result, 200