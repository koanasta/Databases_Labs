# models/repair.py
class Repair:
    def __init__(self, idrepairs=None, equipment_id=None, client_id=None, start_date=None, end_date=None, status=None):
        self.idrepairs = idrepairs
        self.equipment_id = equipment_id
        self.client_id = client_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def to_dict(self):
        return {
            "idrepairs": self.idrepairs,
            "equipment_id": self.equipment_id,
            "client_id": self.client_id,
            "start_date": str(self.start_date) if self.start_date else None,
            "end_date": str(self.end_date) if self.end_date else None,
            "status": self.status
        }
