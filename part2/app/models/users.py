import uuid
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def register(self):
        pass


    def updateProfile(self):
        self.updated_at = datetime.now()


    def delete(self):
        pass
