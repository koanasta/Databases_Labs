# controllers/repairs_controller.py
from flask import Blueprint, request, jsonify
from services.repairs_service import RepairsService
from dto.repair_dto import RepairDTO

repairs_bp = Blueprint("repairs_bp", __name__, url_prefix="/repairs")
service = RepairsService()

@repairs_bp.route("", methods=["GET"])
def get_all():
    repairs = service.list_repairs()
    return jsonify([RepairDTO.from_model(r).to_dict() for r in repairs]), 200

@repairs_bp.route("/<int:repair_id>", methods=["GET"])
def get_one(repair_id):
    try:
        r = service.get_repair(repair_id)
        return jsonify(RepairDTO.from_model(r).to_dict()), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

@repairs_bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    new_id = service.create_repair(data)
    return jsonify({"idrepairs": new_id}), 201

@repairs_bp.route("/<int:repair_id>", methods=["PUT"])
def update(repair_id):
    data = request.get_json()
    try:
        updated = service.update_repair(repair_id, data)
        return jsonify({"updated_rows": updated}), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

@repairs_bp.route("/<int:repair_id>", methods=["DELETE"])
def delete(repair_id):
    try:
        deleted = service.delete_repair(repair_id)
        return jsonify({"deleted_rows": deleted}), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

# ---------- M:1 ----------
@repairs_bp.route("/<int:repair_id>/equipment", methods=["GET"])
def get_equipment(repair_id):
    return jsonify(service.get_equipment(repair_id)), 200

@repairs_bp.route("/<int:repair_id>/client", methods=["GET"])
def get_client(repair_id):
    return jsonify(service.get_client(repair_id)), 200

# ---------- 1:M ----------
@repairs_bp.route("/<int:repair_id>/jobs", methods=["GET"])
def get_jobs(repair_id):
    return jsonify(service.get_jobs(repair_id)), 200
