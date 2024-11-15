from app.models.baseModel import BaseModel
from app import db
from sqlalchemy import CheckConstraint
import uuid

class Review(BaseModel):
    __tablename__ = 'reviews'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer(100), nullable=False)
    self.place_id = place_id

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'owner_id': self.owner_id,
            'place_id': self.place_id
        }
    
    def set_rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
