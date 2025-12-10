# dto/spare_part_dto.py
class SparePartDTO:
    def __init__(self, idspare_parts, name, price, stock_quantity):
        self.idspare_parts = idspare_parts
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    @staticmethod
    def from_model(sp):
        d = sp.to_dict()
        return SparePartDTO(
            d["idspare_parts"],
            d["name"],
            d["price"],
            d["stock_quantity"]
        )

    def to_dict(self):
        return {
            "idspare_parts": self.idspare_parts,
            "name": self.name,
            "price": self.price,
            "stock_quantity": self.stock_quantity
        }
