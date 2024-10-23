from app.persistence.repository import InMemoryRepository
from app.models.users import User
<<<<<<< HEAD
=======
from app.models.places import Place
from app.models.amenities import Amenity
>>>>>>> 694edfc62db2385b0cff05c54d3ae6cebb115ab9
from app.models.reviews import Review

class HBnBFacade:
    _instance = None

    # méthode spéciale __new__ garantit que seule une instance de HBnBFacade sera créée
    def __new__(cls, *args, **kwargs):
        """Override __new__ to control instance creation (Singleton)."""
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "user_repo"):
            self.user_repo = InMemoryRepository()
            self.place_repo = InMemoryRepository()
            self.review_repo = InMemoryRepository()
            self.amenity_repo = InMemoryRepository()

#UPDATE_USER##############################################################################################################

    def create_user(self, user_data):
        """Create an user."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve user's data."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
<<<<<<< HEAD
        return self.user_repo.get_by_attribute('email', email)
    
    def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
    # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get_by_attribute('id', review_id)

    def get_all_reviews(self):
    # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all

    def get_reviews_by_place(self, place_id):
    # Placeholder for logic to retrieve all reviews for a specific place
        return self.review_repo.get_by_attribute('review', place_id)

    def update_review(self, review_id, review_data):
    # Placeholder for logic to update a review
        return self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
    # Placeholder for logic to delete a review
        return self.review_repo.delete(review_id)
=======
        """Retrieve user by mail."""
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

##########################################################################################################################
>>>>>>> 694edfc62db2385b0cff05c54d3ae6cebb115ab9
