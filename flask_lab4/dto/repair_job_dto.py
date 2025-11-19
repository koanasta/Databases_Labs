# dto/repair_job_dto.py
class RepairJobDTO:
    def __init__(self, idrepair_jobs, repair_id, repair_type_id, cost, master_id):
        self.idrepair_jobs = idrepair_jobs
        self.repair_id = repair_id
        self.repair_type_id = repair_type_id
        self.cost = cost
        self.master_id = master_id

    @staticmethod
    def from_model(rj):
        d = rj.to_dict()
        return RepairJobDTO(
            d["idrepair_jobs"],
            d["repair_id"],
            d["repair_type_id"],
            d["cost"],
            d["master_id"]
        )

    def to_dict(self):
        return {
            "idrepair_jobs": self.idrepair_jobs,
            "repair_id": self.repair_id,
            "repair_type_id": self.repair_type_id,
            "cost": self.cost,
            "master_id": self.master_id
        }
