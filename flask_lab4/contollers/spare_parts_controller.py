# controllers/spare_parts_controller.py
from flask import Blueprint, request, jsonify
from services.spare_parts_service import SparePartsService
from dto.spare_part_dto import SparePartDTO

spare_parts_bp = Blueprint("spare_parts_bp", __name__, url_prefix="/spare_parts")
service = SparePartsService()

@spare_parts_bp.route("", methods=["GET"])
def get_all():
    parts = service.list_parts()
    return jsonify([SparePartDTO.from_model(p).to_dict() for p in parts]), 200

@spare_parts_bp.route("/<int:part_id>", methods=["GET"])
def get_one(part_id):
    try:
        part = service.get_part(part_id)
        return jsonify(SparePartDTO.from_model(part).to_dict()), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

@spare_parts_bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    new_id = service.create_part(data)
    return jsonify({"idspare_parts": new_id}), 201

@spare_parts_bp.route("/<int:part_id>", methods=["PUT"])
def update(part_id):
    data = request.get_json()
    try:
        updated = service.update_part(part_id, data)
        return jsonify({"updated_rows": updated}), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

@spare_parts_bp.route("/<int:part_id>", methods=["DELETE"])
def delete(part_id):
    try:
        deleted = service.delete_part(part_id)
        return jsonify({"deleted_rows": deleted}), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404
