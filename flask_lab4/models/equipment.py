# models/equipment.py
class Equipment:
    def __init__(self, idequipment=None, serial_number=None, manufacturer_id=None, equipment_type_id=None, model=None, warranty_until=None):
        self.idequipment = idequipment
        self.serial_number = serial_number
        self.manufacturer_id = manufacturer_id
        self.equipment_type_id = equipment_type_id
        self.model = model
        self.warranty_until = warranty_until

    def to_dict(self):
        return {
            "idequipment": self.idequipment,
            "serial_number": self.serial_number,
            "manufacturer_id": self.manufacturer_id,
            "equipment_type_id": self.equipment_type_id,
            "model": self.model,
            "warranty_until": str(self.warranty_until) if self.warranty_until else None
        }
