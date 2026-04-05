from flask import Blueprint, request, jsonify
from middleware.role_required import role_required
from services.user_service import create_user, get_users, update_user

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users", methods=["POST"])
@role_required(["admin"])  # only admin can create users
def add_user():
    data = request.json
    result, status = create_user(data)
    return jsonify(result), status


@user_bp.route("/users", methods=["GET"])
@role_required(["admin"])
def fetch_users():
    result, status = get_users()
    return jsonify(result), status


@user_bp.route("/users/<int:user_id>", methods=["PATCH"])
@role_required(["admin"])
def edit_user(user_id):
    data = request.json
    result, status = update_user(user_id, data)
    return jsonify(result), status