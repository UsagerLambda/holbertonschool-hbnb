import unittest
from app.models.places import Place  # Assurez-vous d'importer la classe Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Utilisez des valeurs de test pour tous les attributs requis, y compris owner_id
        self.place = Place(
            title="Un bel endroit",
            description="Une description d'un bel endroit.",
            price=100.0,
            latitude=10.0,
            longitude=20.0,
            owner_id="12345"  # Ajoutez une valeur valide pour owner_id
        )

    def test_create_place(self):
        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.title, "Un bel endroit")

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            self.place.title = ""  # Cela doit lever une exception

    def test_invalid_latitude_too_high(self):
        with self.assertRaises(ValueError):
            self.place.latitude = 95.0  # Latitude invalide

    # Ajoutez d'autres tests selon vos besoins

if __name__ == "__main__":
    unittest.main()
