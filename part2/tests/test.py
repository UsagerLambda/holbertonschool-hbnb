import unittest
from app import create_app
import uuid

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

###################################################################USERS

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_for_place(self):
        unique_email = f"jane_{uuid.uuid4()}@example.com"
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jan",
            "last_name": "Doee",
            "email": unique_email  # Email aléatoire pour éviter les conflits
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)  # Vérifie la présence de "id" à la racine de la réponse
        return data["id"]
###################################################################PLACES

    def test_create_place_with_valid_user_id(self):
        # Crée un utilisateur et récupère son ID
        user_id = self.test_create_user_for_place()

        # Utilise cet ID pour créer un `place`
        response = self.client.post('/api/v1/places/', json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": user_id
        })

        # Vérifie si la création du `place` est réussie
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data["place"])

    def test_create_place_invalid_data(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "Cozyy Apartment",
            "description": "A nice place to stay",
            "price": 1,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "1"
        })
        self.assertEqual(response.status_code, 400)

###################################################################AMENITY

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Piscine"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_invalid_data(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)

###################################################################REVIEWS

    def test_create_review(self):
        # Créer un utilisateur pour obtenir l'ID
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Alice",
            "last_name": "Smith",
            "email": f"alice_{uuid.uuid4()}@example.com"  # Email unique
        })
        self.assertEqual(response_user.status_code, 201)
        user_data = response_user.get_json()
        user_id = user_data["id"]

        # Créer un endroit (place) pour obtenir l'ID
        response_place = self.client.post('/api/v1/places/', json={
            "title": "Charming Cottage",
            "description": "A lovely place to stay",
            "price": 150,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": user_id
        })
        self.assertEqual(response_place.status_code, 201)
        place_data = response_place.get_json()
        place_id = place_data["place"]["id"]

        # Créer une review
        response_review = self.client.post('/api/v1/reviews/', json={
            "text": "Piscine",
            "rating": 4,
            "owner_id": user_id,
            "place_id": place_id
        })

        # Vérifier si la création de la review a réussi
        self.assertEqual(response_review.status_code, 201)
        review_data = response_review.get_json()

        # Vérifie la présence de "id" dans le sous-dictionnaire "review"
        self.assertIn("id", review_data["review"])  # Correction ici

    def test_create_review(self):
        # Créer un utilisateur pour obtenir l'ID
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Alice",
            "last_name": "Smith",
            "email": f"alice_{uuid.uuid4()}@example.com"  # Email unique
        })
        self.assertEqual(response_user.status_code, 201)
        user_data = response_user.get_json()
        user_id = user_data["id"]

        # Créer un endroit (place) pour obtenir l'ID
        response_place = self.client.post('/api/v1/places/', json={
            "title": "Charming Cottage",
            "description": "A lovely place to stay",
            "price": 150,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": user_id
        })
        self.assertEqual(response_place.status_code, 201)
        place_data = response_place.get_json()
        place_id = place_data["place"]["id"]

        # Créer une review
        response_review = self.client.post('/api/v1/reviews/', json={
            "text": "Piscine",
            "rating": 4,
            "owner_id": 1,
            "place_id": place_id
        })

        self.assertEqual(response_review.status_code, 400)

