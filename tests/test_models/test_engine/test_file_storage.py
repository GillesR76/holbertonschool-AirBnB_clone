#!/usr/bin/python3


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open('file.json', 'r') as file:
            self.assertIn(obj.id, file.read())

    def test_reload(self):
        # Create a new object and save it
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()

        # Clear the __objects dictionary and reload from file
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        # Check if the object was correctly loaded
        obj_key = "BaseModel." + base_model.id
        self.assertIn(obj_key, self.storage._FileStorage__objects)

        # Remove the file and try to reload
        os.remove(self.file_path)
        try:
            self.storage.reload()
        except FileNotFoundError:
            self.fail("FileNotFoundError was raised")


if __name__ == "__main__":
    unittest.main()
