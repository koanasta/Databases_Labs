# services/equipment_type_service.py
from dao.equipment_type_dao import EquipmentTypeDAO
from models.equipment_type import EquipmentType

class EquipmentTypeService:

    def __init__(self):
        self.dao = EquipmentTypeDAO()

    def list_all(self):
        return self.dao.get_all()

    def get(self, id):
        return self.dao.get_by_id(id)

    def create(self, data):
        et = EquipmentType(
            name=data.get("name"),
            description=data.get("description")
        )
        return self.dao.create(et)

    def update(self, id, data):
        et = EquipmentType(
            name=data.get("name"),
            description=data.get("description")
        )
        return self.dao.update(id, et)

    def delete(self, id):
        return self.dao.delete(id)
