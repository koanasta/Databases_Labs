# dto/equipment_dto.py
class EquipmentDTO:
    def __init__(self, idequipment, serial_number, manufacturer_id,
                 equipment_type_id, model, warranty_until):
        self.idequipment = idequipment
        self.serial_number = serial_number
        self.manufacturer_id = manufacturer_id
        self.equipment_type_id = equipment_type_id
        self.model = model
        self.warranty_until = warranty_until

    @staticmethod
    def from_model(e):
        d = e.to_dict()
        return EquipmentDTO(
            d["idequipment"],
            d["serial_number"],
            d["manufacturer_id"],
            d["equipment_type_id"],
            d["model"],
            d["warranty_until"]
        )

    def to_dict(self):
        return {
            "idequipment": self.idequipment,
            "serial_number": self.serial_number,
            "manufacturer_id": self.manufacturer_id,
            "equipment_type_id": self.equipment_type_id,
            "model": self.model,
            "warranty_until": self.warranty_until
        }
