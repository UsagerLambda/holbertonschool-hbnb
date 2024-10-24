from app.models.baseModel import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, place_id, user, user_id):
        super().__init__()
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        self.text = text
        self.rating = rating
        self.place = place
        self.place_id = place_id
        self.user = user
        self.user_id = user_id

def to_dict(self):
    return {

        "text": self.text,
        "rating": self.rating,
        "place": self.place,
        "place_id": self.place_id,
        "user": self.user,
        "user_id": self.user_id
    }