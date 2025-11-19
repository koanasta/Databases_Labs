class RepairJobSparePart:
    def __init__(self, repair_job_id, spare_part_id, quantity):
        self.repair_job_id = repair_job_id
        self.spare_part_id = spare_part_id
        self.quantity = quantity

    def to_dict(self):
        return {
            "repair_job_id": self.repair_job_id,
            "spare_part_id": self.spare_part_id,
            "quantity": self.quantity
        }
