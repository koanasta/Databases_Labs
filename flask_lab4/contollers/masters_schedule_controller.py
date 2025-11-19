# controllers/masters_schedule_controller.py
from flask import Blueprint, request, jsonify
from services.masters_schedule_service import MastersScheduleService
from dto.masters_schedule_dto import MastersScheduleDTO

masters_schedule_bp = Blueprint("masters_schedule_bp", __name__, url_prefix="/masters_schedule")
service = MastersScheduleService()

@masters_schedule_bp.route("", methods=["GET"])
def get_all():
    rows = service.list_all()
    return jsonify([MastersScheduleDTO.from_model(r).to_dict() for r in rows]), 200

@masters_schedule_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    r = service.get(id)
    return (jsonify(MastersScheduleDTO.from_model(r).to_dict()), 200) if r else (jsonify({"error": "Not found"}), 404)

@masters_schedule_bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    new_id = service.create(data)
    return jsonify({"id": new_id}), 201

@masters_schedule_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    updated = service.update(id, data)
    return jsonify({"updated": updated}), 200

@masters_schedule_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    deleted = service.delete(id)
    return jsonify({"deleted": deleted}), 200
