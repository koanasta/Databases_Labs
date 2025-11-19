# controllers/masters_controller.py
from flask import Blueprint, request, jsonify
from services.masters_service import MastersService
from dto.masters_dto import MasterDTO

masters_bp = Blueprint('masters_bp', __name__, url_prefix='/masters')
service = MastersService()

@masters_bp.route('', methods=['GET'])
def get_masters():
    masters = service.list_masters()
    return jsonify([MasterDTO.from_model(m).to_dict() for m in masters]), 200

@masters_bp.route('/<int:master_id>', methods=['GET'])
def get_master(master_id):
    try:
        m = service.get_master(master_id)
        return jsonify(MasterDTO.from_model(m).to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@masters_bp.route('', methods=['POST'])
def create_master():
    data = request.get_json()
    try:
        new_id = service.create_master(data)
        return jsonify({"idmasters": new_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@masters_bp.route('/<int:master_id>', methods=['PUT'])
def update_master(master_id):
    data = request.get_json()
    try:
        updated = service.update_master(master_id, data)
        return jsonify({"updated_rows": updated}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@masters_bp.route('/<int:master_id>', methods=['DELETE'])
def delete_master(master_id):
    try:
        deleted = service.delete_master(master_id)
        return jsonify({"deleted_rows": deleted}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# M:1 endpoint: all repair_jobs for this master
@masters_bp.route('/<int:master_id>/jobs', methods=['GET'])
def master_jobs(master_id):
    jobs = service.get_jobs(master_id)
    return jsonify(jobs), 200

# M:1 endpoint: schedule for this master
@masters_bp.route('/<int:master_id>/schedule', methods=['GET'])
def master_schedule(master_id):
    schedule = service.get_schedule(master_id)
    return jsonify(schedule), 200
