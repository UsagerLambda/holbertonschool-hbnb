import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def name_length(self, name):
        if len(name) > 50:
            return (name + " ne doit pas dépasser 50 caractères."), 403
        return name

    def place_length(self, place):
        if len(place) > 100:
            return (place + " ne doit pas dépasser 100 caractères."), 403
        return place

