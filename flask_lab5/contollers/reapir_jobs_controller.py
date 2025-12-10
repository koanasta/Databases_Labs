from flask import Blueprint, jsonify
from dao.repair_jobs_dao import RepairJobsDAO

repair_jobs_bp = Blueprint('repair_jobs_bp', __name__, url_prefix='/repair_jobs')
dao = RepairJobsDAO()

@repair_jobs_bp.route('/<int:repair_job_id>/spare_parts', methods=['GET'])
def spare_parts_for_job(repair_job_id):
    parts = dao.get_spare_parts_for_repair_job(repair_job_id)
    return jsonify(parts), 200
