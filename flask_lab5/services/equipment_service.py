# services/equipment_service.py
from dao.equipment_dao import EquipmentDAO
from models.equipment import Equipment

class EquipmentService:
    def __init__(self):
        self.dao = EquipmentDAO()

    def list_equipment(self):
        return self.dao.get_all()

    def get_equipment(self, eq_id):
        eq = self.dao.get_by_id(eq_id)
        if not eq:
            raise ValueError("Equipment not found")
        return eq

    def create_equipment(self, data):
        eq = Equipment(
            serial_number=data.get("serial_number"),
            manufacturer_id=data.get("manufacturer_id"),
            equipment_type_id=data.get("equipment_type_id"),
            model=data.get("model"),
            warranty_until=data.get("warranty_until")
        )
        return self.dao.create(eq)

    def update_equipment(self, eq_id, data):
        existing = self.dao.get_by_id(eq_id)
        if not existing:
            raise ValueError("Equipment not found")

        eq = Equipment(
            serial_number=data.get("serial_number", existing.serial_number),
            manufacturer_id=data.get("manufacturer_id", existing.manufacturer_id),
            equipment_type_id=data.get("equipment_type_id", existing.equipment_type_id),
            model=data.get("model", existing.model),
            warranty_until=data.get("warranty_until", existing.warranty_until)
        )
        return self.dao.update(eq_id, eq)

    def delete_equipment(self, eq_id):
        if not self.dao.get_by_id(eq_id):
            raise ValueError("Equipment not found")
        return self.dao.delete(eq_id)

    def get_manufacturer(self, eq_id):
        return self.dao.get_manufacturer(eq_id)

    def get_equipment_type(self, eq_id):
        return self.dao.get_equipment_type(eq_id)

    def get_repairs(self, eq_id):
        return self.dao.get_repairs(eq_id)
