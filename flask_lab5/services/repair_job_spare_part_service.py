# services/repair_job_spare_part_service.py
from dao.repair_job_spare_part_dao import RepairJobSparePartDAO
from models.reapir_job_spare_part import RepairJobSparePart

class RepairJobSparePartService:

    def __init__(self):
        self.dao = RepairJobSparePartDAO()

    def add(self, data):
        m = RepairJobSparePart(
            repair_job_id=data.get("repair_job_id"),
            spare_part_id=data.get("spare_part_id"),
            quantity=data.get("quantity")
        )
        return self.dao.add_spare_part(m)

    def update(self, repair_job_id, spare_part_id, quantity):
        return self.dao.update_quantity(repair_job_id, spare_part_id, quantity)

    def delete(self, repair_job_id, spare_part_id):
        return self.dao.delete_spare_part(repair_job_id, spare_part_id)

    def list_for_job(self, repair_job_id):
        return self.dao.get_all_for_job(repair_job_id)
