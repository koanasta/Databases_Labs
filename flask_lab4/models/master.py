class Master:
    def __init__(self, idmaster, name, surname, phone, experience_years):
        self.idmaster = idmaster
        self.name = name
        self.surname = surname
        self.phone = phone
        self.experience_years = experience_years

    def to_dict(self):
        return {
            "idmaster": self.idmaster,
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "experience_years": self.experience_years
        }
