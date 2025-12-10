# dto/repair_job_spare_part_dto.py
class RepairJobSparePartDTO:
    def __init__(self, repair_job_id, spare_part_id, quantity):
        self.repair_job_id = repair_job_id
        self.spare_part_id = spare_part_id
        self.quantity = quantity

    @staticmethod
    def from_model(m):
        d = m.to_dict()
        return RepairJobSparePartDTO(
            d["repair_job_id"],
            d["spare_part_id"],
            d["quantity"]
        )

    def to_dict(self):
        return {
            "repair_job_id": self.repair_job_id,
            "spare_part_id": self.spare_part_id,
            "quantity": self.quantity
        }
