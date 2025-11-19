# services/manufacturer_service.py
from dao.manufacturer_dao import ManufacturerDAO
from models.manufacturer import Manufacturer

class ManufacturerService:

    def __init__(self):
        self.dao = ManufacturerDAO()

    def list_all(self):
        return self.dao.get_all()

    def get(self, id):
        return self.dao.get_by_id(id)

    def create(self, data):
        m = Manufacturer(
            name=data.get("name"),
            country=data.get("country"),
            website=data.get("website"),
            phone=data.get("phone")
        )
        return self.dao.create(m)

    def update(self, id, data):
        m = Manufacturer(
            name=data.get("name"),
            country=data.get("country"),
            website=data.get("website"),
            phone=data.get("phone")
        )
        return self.dao.update(id, m)

    def delete(self, id):
        return self.dao.delete(id)
