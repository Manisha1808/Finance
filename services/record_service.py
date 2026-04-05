from models.record import Record
from database.db import db
from sqlalchemy import or_

def create_record(data, user_id):
    try:
        amount = data.get("amount")
        record_type = data.get("type")

        if amount is None or amount <= 0:
            return {"error": "Amount must be positive"}, 400

        if record_type not in ["income", "expense"]:
            return {"error": "Type must be income or expense"}, 400

        record = Record(
            user_id=user_id,
            amount=amount,
            type=record_type,
            category=data.get("category"),
            date=data.get("date"),
            notes=data.get("notes")
        )

        db.session.add(record)
        db.session.commit()

        return {"message": "Record created"}, 201

    except Exception as e:
        return {"error": str(e)}, 500


def get_records(filters):
    try:
        query = Record.query

        # filters
        if "type" in filters:
            query = query.filter_by(type=filters["type"])

        if "category" in filters:
            query = query.filter_by(category=filters["category"])

        #Search
        search = filters.get("search")
        if search:
               query = query.filter(
                    or_(
                        Record.category.ilike(f"%{search}%"),
                        Record.notes.ilike(f"%{search}%")
                       )
               )

        # pagination
        page = int(filters.get("page", 1))
        limit = int(filters.get("limit", 5))

        paginated = query.paginate(page=page, per_page=limit, error_out=False)

        result = []
        for r in paginated.items:
            result.append({
                "id": r.id,
                "amount": r.amount,
                "type": r.type,
                "category": r.category,
                "date": r.date,
                "notes": r.notes
            })

        return {
            "page": page,
            "limit": limit,
            "total": paginated.total,
            "data": result
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500


def update_record(record_id, data):
    record = Record.query.get(record_id)

    if not record:
        return {"error": "Record not found"}, 404

    if "amount" in data:
        try:
            amount = float(data["amount"])
            if amount <= 0:
                return {"error": "Amount must be positive"}, 400
            record.amount = amount
        except:
            return {"error": "Invalid amount"}, 400

    if "type" in data:
        if data["type"] not in ["income", "expense"]:
            return {"error": "Invalid type"}, 400
        record.type = data["type"]

    record.category = data.get("category", record.category)
    record.date = data.get("date", record.date)
    record.notes = data.get("notes", record.notes)

    db.session.commit()

    return {"message": "Record updated"}, 200

def delete_record(record_id):
    record = Record.query.get(record_id)

    if not record:
        return {"error": "Record not found"}, 404

    db.session.delete(record)
    db.session.commit()

    return {"message": "Record deleted"}, 200