# dto/manufacturer_dto.py
class ManufacturerDTO:
    def __init__(self, idmanufacturers, name, country, website, phone):
        self.idmanufacturers = idmanufacturers
        self.name = name
        self.country = country
        self.website = website
        self.phone = phone

    @staticmethod
    def from_model(m):
        d = m.to_dict()
        return ManufacturerDTO(
            d["idmanufacturers"],
            d["name"],
            d["country"],
            d["website"],
            d["phone"]
        )

    def to_dict(self):
        return {
            "idmanufacturers": self.idmanufacturers,
            "name": self.name,
            "country": self.country,
            "website": self.website,
            "phone": self.phone
        }
