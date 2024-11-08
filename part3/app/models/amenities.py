from app.models.baseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        # Vérification que le nom n'est pas vide
        if not name or not name.strip():
            raise ValueError("Field 'name' cannot be empty.")
        valid_name = self.name_length('name', name, 50)
        if isinstance(valid_name, tuple):
            raise ValueError(valid_name[0])
        self.name = name

    def update(self, data):
        if 'name' in data:
            # Vérification que le nom n'est pas vide
            if not data['name'] or not data['name'].strip():
                raise ValueError("Field 'name' cannot be empty.")
            valid_name = self.name_length('name', data['name'], 50)
            if isinstance(valid_name, tuple):
                raise ValueError(valid_name[0])
            self.name = data['name']

    def to_dict(self):
        """Convert the Amenity object into a dictionary."""
        return {
            'name': self.name
        }
