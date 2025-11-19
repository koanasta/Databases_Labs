# controllers/repair_jobs_controller.py
from flask import Blueprint, request, jsonify
from services.repair_jobs_service import RepairJobsService
from dto.repair_job_dto import RepairJobDTO

repair_jobs_bp = Blueprint("repair_jobs_bp", __name__, url_prefix="/repair_jobs")
service = RepairJobsService()

@repair_jobs_bp.route("", methods=["GET"])
def get_all():
    jobs = service.list_jobs()
    return jsonify([RepairJobDTO.from_model(j).to_dict() for j in jobs]), 200

@repair_jobs_bp.route("/<int:job_id>", methods=["GET"])
def get_one(job_id):
    try:
        j = service.get_job(job_id)
        return jsonify(RepairJobDTO.from_model(j).to_dict()), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

@repair_jobs_bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    new_id = service.create_job(data)
    return jsonify({"idrepair_jobs": new_id}), 201

@repair_jobs_bp.route("/<int:job_id>", methods=["PUT"])
def update(job_id):
    data = request.get_json()
    try:
        updated = service.update_job(job_id, data)
        return jsonify({"updated_rows": updated}), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

@repair_jobs_bp.route("/<int:job_id>", methods=["DELETE"])
def delete(job_id):
    try:
        deleted = service.delete_job(job_id)
        return jsonify({"deleted_rows": deleted}), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 404

# ---------- M:1 ----------
@repair_jobs_bp.route("/<int:job_id>/repair", methods=["GET"])
def get_repair(job_id):
    return jsonify(service.get_repair(job_id)), 200

@repair_jobs_bp.route("/<int:job_id>/type", methods=["GET"])
def get_type(job_id):
    return jsonify(service.get_type(job_id)), 200

@repair_jobs_bp.route("/<int:job_id>/master", methods=["GET"])
def get_master(job_id):
    return jsonify(service.get_master(job_id)), 200

# ---------- M:M ----------
@repair_jobs_bp.route("/<int:job_id>/spare_parts", methods=["GET"])
def get_spare_parts(job_id):
    return jsonify(service.get_spare_parts(job_id)), 200
