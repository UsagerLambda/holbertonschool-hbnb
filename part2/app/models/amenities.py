from datetime import datetime
import uuid

class Amenity:
    def __init__(self, name, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description

    def createAmenity(self):
        pass


    def updateAmenity(self):
        self.updated_at = datetime.now()


    def deleteAmenity(self):
        pass


    def listAmenity(self):
        pass
