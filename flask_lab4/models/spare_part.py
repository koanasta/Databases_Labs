# models/spare_part.py
class SparePart:
    def __init__(self, idspare_parts=None, name=None, manufacturer_id=None, equipment_type_id=None, price=None, stock_quantity=None):
        self.idspare_parts = idspare_parts
        self.name = name
        self.manufacturer_id = manufacturer_id
        self.equipment_type_id = equipment_type_id
        self.price = price
        self.stock_quantity = stock_quantity

    def to_dict(self):
        return {
            "idspare_parts": self.idspare_parts,
            "name": self.name,
            "manufacturer_id": self.manufacturer_id,
            "equipment_type_id": self.equipment_type_id,
            "price": self.price,
            "stock_quantity": self.stock_quantity
        }
