from app.models.baseModel import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        valid_first_name = self.name_length(first_name)
        valid_last_name = self.name_length(last_name)
        if isinstance(valid_first_name, tuple):
            raise ValueError(valid_first_name[0])
        if isinstance(valid_last_name, tuple):
            raise ValueError(valid_last_name[0])
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.place = []


    def add_place(self, place):
        self.place.append(place)


    def updateProfile(self, data):
        if isinstance(data, dict):
            self.update(data)
        else:
            raise TypeError("Les données passées doivent être un dictionnaire.")
