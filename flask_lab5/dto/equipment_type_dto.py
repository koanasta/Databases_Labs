# dto/equipment_type_dto.py
class EquipmentTypeDTO:
    def __init__(self, idequipment_types, name, description):
        self.idequipment_types = idequipment_types
        self.name = name
        self.description = description

    @staticmethod
    def from_model(m):
        d = m.to_dict()
        return EquipmentTypeDTO(
            d["idequipment_types"],
            d["name"],
            d["description"]
        )

    def to_dict(self):
        return {
            "idequipment_types": self.idequipment_types,
            "name": self.name,
            "description": self.description
        }
