# controllers/equipment_type_controller.py
from flask import Blueprint, request, jsonify
from services.equipment_type_service import EquipmentTypeService
from dto.equipment_type_dto import EquipmentTypeDTO

equipment_type_bp = Blueprint("equipment_type_bp", __name__, url_prefix="/equipment_types")
service = EquipmentTypeService()

@equipment_type_bp.route("", methods=["GET"])
def get_all():
    rows = service.list_all()
    return jsonify([EquipmentTypeDTO.from_model(r).to_dict() for r in rows]), 200

@equipment_type_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    r = service.get(id)
    return (jsonify(EquipmentTypeDTO.from_model(r).to_dict()), 200) if r else (jsonify({"error": "Not found"}), 404)

@equipment_type_bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    new_id = service.create(data)
    return jsonify({"id": new_id}), 201

@equipment_type_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    updated = service.update(id, data)
    return jsonify({"updated": updated}), 200

@equipment_type_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    deleted = service.delete(id)
    return jsonify({"deleted": deleted}), 200
