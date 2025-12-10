# dto/repair_dto.py
class RepairDTO:
    def __init__(self, idrepairs, equipment_id, client_id, start_date, end_date, status):
        self.idrepairs = idrepairs
        self.equipment_id = equipment_id
        self.client_id = client_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    @staticmethod
    def from_model(r):
        d = r.to_dict()
        return RepairDTO(
            d["idrepairs"],
            d["equipment_id"],
            d["client_id"],
            d["start_date"],
            d["end_date"],
            d["status"]
        )

    def to_dict(self):
        return {
            "idrepairs": self.idrepairs,
            "equipment_id": self.equipment_id,
            "client_id": self.client_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status
        }
