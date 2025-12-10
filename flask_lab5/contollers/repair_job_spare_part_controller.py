# controllers/repair_job_spare_part_controller.py
from flask import Blueprint, request, jsonify
from services.repair_job_spare_part_service import RepairJobSparePartService
from dto.repair_job_spare_part_dto import RepairJobSparePartDTO

rjsp_bp = Blueprint("rjsp_bp", __name__, url_prefix="/repair_job_spare_part")
service = RepairJobSparePartService()

# ADD spare part to job
@rjsp_bp.route("", methods=["POST"])
def add_part():
    data = request.get_json()
    added = service.add(data)
    return jsonify({"updated_rows": added}), 201

# UPDATE quantity
@rjsp_bp.route("/<int:repair_job_id>/<int:spare_part_id>", methods=["PUT"])
def update(repair_job_id, spare_part_id):
    data = request.get_json()
    updated = service.update(repair_job_id, spare_part_id, data.get("quantity"))
    return jsonify({"updated_rows": updated}), 200

# DELETE part from job
@rjsp_bp.route("/<int:repair_job_id>/<int:spare_part_id>", methods=["DELETE"])
def delete(repair_job_id, spare_part_id):
    deleted = service.delete(repair_job_id, spare_part_id)
    return jsonify({"deleted_rows": deleted}), 200

# GET all parts for a job
@rjsp_bp.route("/<int:repair_job_id>", methods=["GET"])
def list_for_job(repair_job_id):
    rows = service.list_for_job(repair_job_id)
    return jsonify([RepairJobSparePartDTO.from_model(r).to_dict() for r in rows]), 200
