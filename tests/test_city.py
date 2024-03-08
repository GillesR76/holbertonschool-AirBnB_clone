#!/usr/bin/python3


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_instance(self):
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_str(self):
        expected_output = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_output)

    def test_save(self):
        original_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

        new_city = City()
        new_city.save()
        with open('file.json', 'r') as file:
            self.assertIn("City." + new_city.id, file.read())

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["id"], self.city.id)
        self.assertEqual(city_dict["created_at"],
                         self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"],
                         self.city.updated_at.isoformat())
