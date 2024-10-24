from app.models.baseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        valid_name = self.name_length(name)
        if isinstance(valid_name, tuple):
            raise ValueError(valid_name[0])
        self.name = name

    def update(self, data):
        if 'name' in data:
            valid_name = self.name_length(data['name'])
            if isinstance(valid_name, tuple):
                raise ValueError(valid_name[0])
            self.name = data['name']

    def to_dict(self):
        return {'name': self.name}
