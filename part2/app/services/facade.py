from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.reviews import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Placeholder method for fetching a user by ID
    def get_user(self, user_id):
        # Logic will be implemented in later tasks
        return self.user_repo.get(user_id)
    
    # Method for fetching a user by email
    def get_user_by_email(self, email):
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