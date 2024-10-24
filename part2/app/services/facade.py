from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.places import Place
from app.models.amenities import Amenity
from app.models.reviews import Review


class HBnBFacade:
    def __init__(self):
        if not hasattr(self, "user_repo"):
            self.user_repo = InMemoryRepository()
            self.place_repo = InMemoryRepository()
            self.review_repo = InMemoryRepository()
            self.amenity_repo = InMemoryRepository()

# ######USER##############################################################################################################

    def create_user(self, user_data):
        """Create an user."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve user's data."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """Retrieve all users."""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """Update the user's data."""
        user = self.user_repo.get(user_id)
        if not user:
            return None

        user.first_name = user_data.get("first_name", user.first_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.email = user_data.get("email", user.email)

        self.user_repo.update(user_id, {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "is_admin": user.is_admin
        })
        return user
    #############################################################################################################
#REVIEW BLOCK####################################################################################################
    def create_review(self, review_data):
        """Create a review"""
        review = Review(**review_data)
        self.review_repo.add(review)
        return review


    def get_review(self, review_id):
        """Retrieve a review with its ID"""
        return self.review_repo.get( review_id)


    def get_all_reviews(self):
        """Retrieve all users"""
        return self.review_repo.get_all()


    def get_reviews_by_place(self, place_id):
        """Retrieve reviews by place"""
        return self.review_repo.get_by_attribute('review', place_id)


    def update_review(self, review_id, review_data):
        """Update a review"""
        self.review_repo.update(review_id)
         

    def delete_review(self, review_id):
        """Delete a Review"""
        self.review_repo.delete(review_id)
    ###########################################################################################################
# ####PLACES##############################################################################################################

    def create_place(self, place_data):
        """Create an place."""
        try:
            place = Place(**place_data)
            self.place_repo.add(place)
            return place.to_dict()
        except (ValueError, TypeError) as e:
            raise ValueError(f"Failed to create place: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while creating the place: {str(e)}")

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Retrieve all users."""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None

        try:
            self.place_repo.update(place_id, place_data)
            return place
        except Exception as e:
            raise RuntimeError(f"An error occurred while updating the place: {str(e)}")

# ########################################################################################################################
#AMENITIES BLOCK##########################################################################################################
    
    # Method for fetching a user by email
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)


    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity


    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)


    def get_all_amenities(self):
        return self.amenity_repo.get_all()


    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)
#########################################################################################################################