from users import User
from places import Place
from reviews import Review
from amenities import Amenity

"""
    Fichier de test : "python3 test.py" pour l'exécuter
"""

def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default value
    print("\033[32mUser creation test passed!\033[0m")

def test_place_creation():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)

    # Adding a review
    review = Review(text="Great stay!", rating=5, place=place, user=owner)
    place.add_review(review)

    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert len(place.reviews) == 1
    assert place.reviews[0].text == "Great stay!"
    print("\033[32mPlace creation and relationship test passed!\033[0m")

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("\033[32mAmenity creation test passed!\033[0m")

test_user_creation()
test_place_creation()
test_amenity_creation()
