class EquipmentType:
    def __init__(self, idequipment_type, name, description):
        self.idequipment_type = idequipment_type
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "idequipment_type": self.idequipment_type,
            "name": self.name,
            "description": self.description
        }
