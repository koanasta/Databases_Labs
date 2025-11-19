# models/repair_job.py
class RepairJob:
    def __init__(self, idrepair_jobs=None, repair_id=None, repair_type_id=None, cost=None, master_id=None):
        self.idrepair_jobs = idrepair_jobs
        self.repair_id = repair_id
        self.repair_type_id = repair_type_id
        self.cost = cost
        self.master_id = master_id

    def to_dict(self):
        return {
            "idrepair_jobs": self.idrepair_jobs,
            "repair_id": self.repair_id,
            "repair_type_id": self.repair_type_id,
            "cost": self.cost,
            "master_id": self.master_id
        }
