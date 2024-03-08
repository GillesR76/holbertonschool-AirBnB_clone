#!/usr/bin/python3


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_instance(self):
        attributes = {
            "name": "",
            "city_id": "",
            "user_id": "",
            "description": "",
            "number_rooms": 0,
            "number_bathrooms": 0,
            "max_guest": 0,
            "price_by_night": 0,
            "latitude": 0.0,
            "longitude": 0.0,
            "amenity_ids": []
        }
        for attr, expected_value in attributes.items():
            self.assertEqual(getattr(self.place, attr), expected_value)

    def test_str(self):
        expected_output = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_output)

    def test_save(self):
        original_updated_at = self.place.updated_at
        self.place.save()
        new_updated_at = self.place.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

        new_place = Place()
        new_place.save()
        with open('file.json', 'r') as file:
            self.assertIn("Place." + new_place.id, file.read())

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], self.place.id)
        self.assertEqual(place_dict["created_at"],
                         self.place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"],
                         self.place.updated_at.isoformat())
