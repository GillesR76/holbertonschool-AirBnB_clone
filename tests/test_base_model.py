#!/usr/bin/python3


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_str(self):
        expected_output = (
            f"[BaseModel] ({self.model.id}) "
            f"{self.model.__dict__}"
        )
        self.assertEqual(str(self.model), expected_output)

    def test_save(self):
        original_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

        new_model = BaseModel()
        new_model.save()
        with open('file.json', 'r') as file:
            self.assertIn("BaseModel." + new_model.id, file.read())

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())
