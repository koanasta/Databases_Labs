# controllers/equipment_controller.py
from flask import Blueprint, request, jsonify
from services.equipment_service import EquipmentService
from dto.equipment_dto import EquipmentDTO

equipment_bp = Blueprint("equipment_bp", __name__, url_prefix="/equipment")
service = EquipmentService()

@equipment_bp.route("", methods=["GET"])
def get_all():
    eqs = service.list_equipment()
    return jsonify([EquipmentDTO.from_model(e).to_dict() for e in eqs]), 200

@equipment_bp.route("/<int:eq_id>", methods=["GET"])
def get_one(eq_id):
    try:
        e = service.get_equipment(eq_id)
        return jsonify(EquipmentDTO.from_model(e).to_dict()), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

@equipment_bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    new_id = service.create_equipment(data)
    return jsonify({"idequipment": new_id}), 201

@equipment_bp.route("/<int:eq_id>", methods=["PUT"])
def update(eq_id):
    data = request.get_json()
    try:
        updated = service.update_equipment(eq_id, data)
        return jsonify({"updated_rows": updated}), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

@equipment_bp.route("/<int:eq_id>", methods=["DELETE"])
def delete(eq_id):
    try:
        deleted = service.delete_equipment(eq_id)
        return jsonify({"deleted_rows": deleted}), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

# ---------- M:1 ----------
@equipment_bp.route("/<int:eq_id>/manufacturer", methods=["GET"])
def get_manufacturer(eq_id):
    return jsonify(service.get_manufacturer(eq_id)), 200

@equipment_bp.route("/<int:eq_id>/type", methods=["GET"])
def get_type(eq_id):
    return jsonify(service.get_equipment_type(eq_id)), 200

# ---------- 1:M ----------
@equipment_bp.route("/<int:eq_id>/repairs", methods=["GET"])
def get_repairs(eq_id):
    return jsonify(service.get_repairs(eq_id)), 200
