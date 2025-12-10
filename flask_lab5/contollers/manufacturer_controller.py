# controllers/manufacturer_controller.py
from flask import Blueprint, request, jsonify
from services.manufacturer_service import ManufacturerService
from dto.manufacturer_dto import ManufacturerDTO

manufacturer_bp = Blueprint("manufacturer_bp", __name__, url_prefix="/manufacturers")
service = ManufacturerService()

@manufacturer_bp.route("", methods=["GET"])
def get_all():
    rows = service.list_all()
    return jsonify([ManufacturerDTO.from_model(r).to_dict() for r in rows]), 200

@manufacturer_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    r = service.get(id)
    return jsonify(ManufacturerDTO.from_model(r).to_dict()), 200 if r else (jsonify({"error": "Not found"}), 404)

@manufacturer_bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    new_id = service.create(data)
    return jsonify({"id": new_id}), 201

@manufacturer_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    updated = service.update(id, data)
    return jsonify({"updated": updated}), 200

@manufacturer_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    deleted = service.delete(id)
    return jsonify({"deleted": deleted}), 200
