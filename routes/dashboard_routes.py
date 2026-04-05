from flask import Blueprint, jsonify
from middleware.role_required import role_required
from services.dashboard_service import (
    get_summary,
    category_wise,
    recent_transactions
)

dashboard_bp = Blueprint("dashboard_bp", __name__)


@dashboard_bp.route("/dashboard/summary", methods=["GET"])
@role_required(["admin", "analyst"])
def summary():
    result, status = get_summary()
    return jsonify(result), status


@dashboard_bp.route("/dashboard/category", methods=["GET"])
@role_required(["admin", "analyst"])
def category():
    result, status = category_wise()
    return jsonify(result), status


@dashboard_bp.route("/dashboard/recent", methods=["GET"])
@role_required(["admin", "analyst"])
def recent():
    result, status = recent_transactions()
    return jsonify(result), status