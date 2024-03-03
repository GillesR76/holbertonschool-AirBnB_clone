#!/usr/bin/python3


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        model_str = self.model.__str__()
        self.assertIsInstance(model_str, str)
        self.assertIn(self.model.__class__.__name__, model_str)
        self.assertIn(self.model.id, model_str)
        self.assertIn('created_at', model_str)
        self.assertIn('updated_at', model_str)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())
