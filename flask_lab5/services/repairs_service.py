# services/repairs_service.py
from dao.repairs_dao import RepairsDAO
from models.repair import Repair

class RepairsService:
    def __init__(self):
        self.dao = RepairsDAO()

    def list_repairs(self):
        return self.dao.get_all()

    def get_repair(self, repair_id):
        r = self.dao.get_by_id(repair_id)
        if not r:
            raise ValueError("Repair not found")
        return r

    def create_repair(self, data):
        r = Repair(
            equipment_id=data.get("equipment_id"),
            client_id=data.get("client_id"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            status=data.get("status")
        )
        return self.dao.create(r)

    def update_repair(self, repair_id, data):
        existing = self.dao.get_by_id(repair_id)
        if not existing:
            raise ValueError("Repair not found")

        r = Repair(
            equipment_id=data.get("equipment_id", existing.equipment_id),
            client_id=data.get("client_id", existing.client_id),
            start_date=data.get("start_date", existing.start_date),
            end_date=data.get("end_date", existing.end_date),
            status=data.get("status", existing.status)
        )
        return self.dao.update(repair_id, r)

    def delete_repair(self, repair_id):
        if not self.dao.get_by_id(repair_id):
            raise ValueError("Repair not found")
        return self.dao.delete(repair_id)

    def get_equipment(self, repair_id):
        return self.dao.get_equipment(repair_id)

    def get_client(self, repair_id):
        return self.dao.get_client(repair_id)

    def get_jobs(self, repair_id):
        return self.dao.get_jobs(repair_id)
