from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.places import Place
from app.models.amenities import Amenity
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

########USER##############################################################################################################

    def create_user(self, user_data):
        """Create an user."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve user's data."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
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
######PLACES##############################################################################################################

    def create_place(self, place_data):
        """Create an place."""
        required_keys = ['title', 'description', 'price', 'latitude', 'longitude', 'owner_id']
        if not all(key in place_data for key in required_keys):
            raise ValueError("Missing required fields: " + ", ".join(required_keys))
        try:
            place = Place(**place_data)
            self.place_repo.add(place)
            return place.to_dict()
        except ValueError as e:
            # Gestion des erreurs de validation
            raise ValueError(f"Failed to create place: {str(e)}")
        except Exception as e:
            # Gestion des autres erreurs
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

        place.title = place_data.get("title", place.title)
        place.description = place_data.get("description", place.description)
        place.price = place_data.get("price", place.price)
        place.latitude = place_data.get("latitude", place.latitude)
        place.longitude = place_data.get("longitude", place.longitude)
        place.owner_id = place_data.get("owner_id", place.owner_id)
        place.reviews = place_data.get("reviews", place.reviews)
        place.amenities = place_data.get("amenities", place.amenities)

        self.place_repo.update(place_id, {
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner_id": place.owner_id,
            "reviews": place.reviews,
            "amenities": place.amenities
        })
        return place

##########################################################################################################################
