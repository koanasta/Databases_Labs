# dto/repair_type_dto.py
class RepairTypeDTO:
    def __init__(self, idrepair_types, name, description):
        self.idrepair_types = idrepair_types
        self.name = name
        self.description = description

    @staticmethod
    def from_model(m):
        d = m.to_dict()
        return RepairTypeDTO(
            d["idrepair_types"],
            d["name"],
            d["description"]
        )

    def to_dict(self):
        return {
            "idrepair_types": self.idrepair_types,
            "name": self.name,
            "description": self.description
        }
