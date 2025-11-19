# dto/masters_dto.py
class MasterDTO:
    def __init__(self, idmasters, full_name, specialization, phone):
        self.idmasters = idmasters
        self.full_name = full_name
        self.specialization = specialization
        self.phone = phone

    @staticmethod
    def from_model(m):
        # m is Master model or dict-like
        if hasattr(m, "to_dict"):
            mm = m.to_dict()
            return MasterDTO(mm.get("idmasters"), mm.get("full_name"), mm.get("specialization"), mm.get("phone"))
        else:
            # if m already a dict
            return MasterDTO(m.get("idmasters"), m.get("full_name"), m.get("specialization"), m.get("phone"))

    def to_dict(self):
        return {
            "idmasters": self.idmasters,
            "full_name": self.full_name,
            "specialization": self.specialization,
            "phone": self.phone
        }
