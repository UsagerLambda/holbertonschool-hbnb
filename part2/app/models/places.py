from datetime import datetime
import uuid

class Place:
    def __init__(self, user_id, title, description, price, latitude, longitude):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def createPlace(self):
        pass


    def deletePlace(self):
        pass


    def listPlace(self):
        pass
