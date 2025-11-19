# services/repair_type_service.py
from dao.repair_type_dao import RepairTypeDAO
from models.repair_type import RepairType

class RepairTypeService:

    def __init__(self):
        self.dao = RepairTypeDAO()

    def list_all(self):
        return self.dao.get_all()

    def get(self, id):
        return self.dao.get_by_id(id)

    def create(self, data):
        rt = RepairType(
            name=data.get("name"),
            description=data.get("description")
        )
        return self.dao.create(rt)

    def update(self, id, data):
        rt = RepairType(
            name=data.get("name"),
            description=data.get("description")
        )
        return self.dao.update(id, rt)

    def delete(self, id):
        return self.dao.delete(id)
