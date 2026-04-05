from flask import Blueprint, request, jsonify
from middleware.role_required import role_required
from services.record_service import (
    create_record,
    get_records,
    update_record,
    delete_record
)

record_bp = Blueprint("record_bp", __name__)


@record_bp.route("/records", methods=["POST"])
@role_required(["admin"])
def add_record():
    print(request.headers)

    data = request.json
    user_id = request.headers.get("User-Id")

    if not user_id:
        return jsonify({"error": "user_id missing"}), 400
    
    user_id = int(user_id)
    result, status = create_record(data, user_id)
    return jsonify(result), status

@record_bp.route("/records", methods=["GET"])
@role_required(["admin", "analyst", "viewer"])  # all can view
def fetch_records():
    filters = request.args.to_dict()
    result, status = get_records(filters)
    return jsonify(result), status


@record_bp.route("/records/<int:record_id>", methods=["PUT"])
@role_required(["admin"])  # only admin
def edit_record(record_id):
    data = request.json
    result, status = update_record(record_id, data)
    return jsonify(result), status


@record_bp.route("/records/<int:record_id>", methods=["DELETE"])
@role_required(["admin"])  # only admin
def remove_record(record_id):
    result, status = delete_record(record_id)
    return jsonify(result), status