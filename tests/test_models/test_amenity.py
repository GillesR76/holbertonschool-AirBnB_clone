#!/usr/bin/python3


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_instance(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
