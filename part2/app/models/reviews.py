from datetime import datetime
import uuid

class Review:
    def __init__(self, user_id, place_id, rating, comment):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def createReview(self):
        pass


    def updateReview(self):
        self.updated_at = datetime.now()


    def deleteReview(self):
        pass


    def listReview(self):
        pass
