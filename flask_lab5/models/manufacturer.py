class Manufacturer:
    def __init__(self, idmanufacturer, name, country):
        self.idmanufacturer = idmanufacturer
        self.name = name
        self.country = country

    def to_dict(self):
        return {
            "idmanufacturer": self.idmanufacturer,
            "name": self.name,
            "country": self.country
        }
