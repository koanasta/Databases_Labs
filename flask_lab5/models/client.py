class Client:
    def __init__(self, idclients=None, full_name=None, phone=None, email=None, registration_date=None):
        self.idclients = idclients
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.registration_date = registration_date

    def to_dict(self):
        return {
            "idclients": self.idclients,
            "full_name": self.full_name,
            "phone": self.phone,
            "email": self.email,
            "registration_date": self.registration_date
        }
