from app.models.baseModel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        self.text = text
        self.user_id = user_id
        self.rating = rating
        self.place = place
        self.user = user

def to_dict(self):
    return {

        "text": self.text,
        "rating": self.rating,
        "place_id": self.rating,
        "user_id": self.user
    }