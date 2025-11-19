class RepairType:
    def __init__(self, idrepair_type, name, price):
        self.idrepair_type = idrepair_type
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "idrepair_type": self.idrepair_type,
            "name": self.name,
            "price": self.price
        }
