from app.models.amenities import Amenity
from app import db
from app.persistence.repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)