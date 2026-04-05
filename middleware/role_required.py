from functools import wraps
from flask import request, jsonify
from models.user import User


def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            user_id = request.headers.get("User-Id")

            if not user_id:
                return jsonify({"error": "User-Id missing"}), 400

            try:
                user_id = int(user_id)
            except:
                return jsonify({"error": "Invalid User-Id"}), 400

            user = User.query.get(user_id)

            if not user:
                return jsonify({"error": "User not found"}), 404

            if not user.is_active:
                return jsonify({"error": "User inactive"}), 403

            if user.role not in allowed_roles:
                return jsonify({"error": "Access denied"}), 403

            return func(*args, **kwargs)

        return wrapper
    return decorator