# services/masters_service.py
from dao.masters_dao import MastersDAO
from models.master import Master

class MastersService:
    def __init__(self):
        self.dao = MastersDAO()

    def list_masters(self):
        return self.dao.get_all()

    def get_master(self, master_id):
        m = self.dao.get_by_id(master_id)
        if not m:
            raise ValueError("Master not found")
        return m

    def create_master(self, data):
        if not data.get("full_name"):
            raise ValueError("full_name is required")
        master = Master(full_name=data.get("full_name"),
                        specialization=data.get("specialization"),
                        phone=data.get("phone"))
        new_id = self.dao.create(master)
        return new_id

    def update_master(self, master_id, data):
        existing = self.dao.get_by_id(master_id)
        if not existing:
            raise ValueError("Master not found")
        master = Master(full_name=data.get("full_name", existing.full_name),
                        specialization=data.get("specialization", existing.specialization),
                        phone=data.get("phone", existing.phone))
        updated_rows = self.dao.update(master_id, master)
        return updated_rows

    def delete_master(self, master_id):
        existing = self.dao.get_by_id(master_id)
        if not existing:
            raise ValueError("Master not found")
        deleted = self.dao.delete(master_id)
        return deleted

    def get_jobs(self, master_id):
        # returns list of repair jobs dicts
        return self.dao.get_jobs_for_master(master_id)

    def get_schedule(self, master_id):
        return self.dao.get_schedule_for_master(master_id)
