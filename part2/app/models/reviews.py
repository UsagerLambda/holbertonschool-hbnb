from baseModel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def createReview(self):
        pass

    def deleteReview(self):
        pass

    def listReview(self):
        pass
