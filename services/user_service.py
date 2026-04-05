from models.user import User
from database.db import db
from sqlalchemy.exc import IntegrityError

def create_user(data):
    if not data.get("name") or not data.get("email") or not data.get("role"):
        return {"error": "Missing fields"}, 400
    try:
          user = User(
                 name=data["name"],
                 email=data["email"],
                 role=data["role"]
      )

          db.session.add(user)
          db.session.commit()

          return {"message": "User created"}, 201
    except IntegrityError:
        db.session.rollback()
        return {"error": "Email already exists"}, 400

    except Exception as e:
        return {"error": str(e)}, 500

def get_users():
    users = User.query.all()

    result = []
    for u in users:
        result.append({
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "role": u.role,
            "is_active": u.is_active
        })

    return result, 200


def update_user(user_id, data):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User not found"}, 404

    user.role = data.get("role", user.role)
    user.is_active = data.get("is_active", user.is_active)

    db.session.commit()

    return {"message": "User updated"}, 200