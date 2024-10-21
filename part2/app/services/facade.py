from app.persistence.repository import InMemoryRepository
from app.models.users import User

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