# services/repair_jobs_service.py
from dao.repair_jobs_dao import RepairJobsDAO
from models.repair_job import RepairJob

class RepairJobsService:
    def __init__(self):
        self.dao = RepairJobsDAO()

    def list_jobs(self):
        return self.dao.get_all()

    def get_job(self, job_id):
        job = self.dao.get_by_id(job_id)
        if not job:
            raise ValueError("Repair job not found")
        return job

    def create_job(self, data):
        job = RepairJob(
            repair_id=data.get("repair_id"),
            repair_type_id=data.get("repair_type_id"),
            cost=data.get("cost"),
            master_id=data.get("master_id")
        )
        return self.dao.create(job)

    def update_job(self, job_id, data):
        existing = self.dao.get_by_id(job_id)
        if not existing:
            raise ValueError("Repair job not found")

        job = RepairJob(
            repair_id=data.get("repair_id", existing.repair_id),
            repair_type_id=data.get("repair_type_id", existing.repair_type_id),
            cost=data.get("cost", existing.cost),
            master_id=data.get("master_id", existing.master_id)
        )
        return self.dao.update(job_id, job)

    def delete_job(self, job_id):
        if not self.dao.get_by_id(job_id):
            raise ValueError("Repair job not found")
        return self.dao.delete(job_id)

    # ---------- M:1 ----------
    def get_repair(self, job_id):
        return self.dao.get_repair(job_id)

    def get_type(self, job_id):
        return self.dao.get_type(job_id)

    def get_master(self, job_id):
        return self.dao.get_master(job_id)

    # ---------- M:M ----------
    def get_spare_parts(self, job_id):
        return self.dao.get_spare_parts(job_id)
