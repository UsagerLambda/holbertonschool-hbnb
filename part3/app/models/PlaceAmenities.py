from app import db
from sqlalchemy.orm import relationship


class PlaceAmenities(db.Model):

    __tablename__ = "placeamenities"

    place_id = db.Column(db.String(36), db.ForeignKey("places.uuid"), primary_key=True)
    amenity_id = db.Column(
        db.String(36), db.ForeignKey("amenities.uuid"), primary_key=True
    )
    place = relationship("Place", back_populates="placeamenities", overlaps="amenities,places")
    amenity = relationship("Amenity", back_populates="amenityplaces", overlaps="amenities,places")