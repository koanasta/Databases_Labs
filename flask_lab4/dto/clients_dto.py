class ClientDTO:
    def __init__(self, idclients, full_name, phone, email, registration_date):
        self.idclients = idclients
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.registration_date = registration_date

    @staticmethod
    def from_model(m):
        d = m.to_dict()
        return ClientDTO(
            d["idclients"],
            d["full_name"],
            d["phone"],
            d["email"],
            d["registration_date"]
        )

    def to_dict(self):
        return {
            "idclients": self.idclients,
            "full_name": self.full_name,
            "phone": self.phone,
            "email": self.email,
            "registration_date": self.registration_date
        }
