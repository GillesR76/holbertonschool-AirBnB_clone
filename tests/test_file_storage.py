#!/usr/bin/python3


"""
This is a new module

"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Tester class

    """
    def setUp(self):
        """
        tester method setup

        """
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Test method tearDown

        """
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_all(self):
        """
        Test method test_all

        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Tester method test new

        """
        self.storage.new(self.base_model)
        self.assertIn('BaseModel.' + self.base_model.id, self.storage.all())

    def test_save(self):
        """
        Test save

        """
        self.storage.new(self.base_model)
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """
        Test reload method

        """
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        self.assertIn('BaseModel.' + self.base_model.id, self.storage.all())


if __name__ == '__main__':
    unittest.main()
