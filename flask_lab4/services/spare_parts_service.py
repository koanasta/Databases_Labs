# services/spare_parts_service.py
from dao.spare_parts_dao import SparePartsDAO
from models.spare_part import SparePart

class SparePartsService:
    def __init__(self):
        self.dao = SparePartsDAO()

    def list_parts(self):
        return self.dao.get_all()

    def get_part(self, part_id):
        part = self.dao.get_by_id(part_id)
        if not part:
            raise ValueError("Spare part not found")
        return part

    def create_part(self, data):
        part = SparePart(
            name=data.get("name"),
            price=data.get("price"),
            stock_quantity=data.get("stock_quantity")
        )
        return self.dao.create(part)

    def update_part(self, part_id, data):
        existing = self.dao.get_by_id(part_id)
        if not existing:
            raise ValueError("Spare part not found")

        part = SparePart(
            name=data.get("name", existing.name),
            price=data.get("price", existing.price),
            stock_quantity=data.get("stock_quantity", existing.stock_quantity)
        )
        return self.dao.update(part_id, part)

    def delete_part(self, part_id):
        if not self.dao.get_by_id(part_id):
            raise ValueError("Spare part not found")
        return self.dao.delete(part_id)
