#!/usr/bin/python3


"""
User class test

"""
import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    """
    User tester class

    """
    def test_init(self):
        """
        This is a method

        """
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict(self):
        """
        This is a other on method
        
        """
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['id'], str)
        self.assertIn('created_at', user_dict)
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIn('updated_at', user_dict)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertIn('email', user_dict)
        self.assertIsInstance(user_dict['email'], str)
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertIn('password', user_dict)
        self.assertIsInstance(user_dict['password'], str)
        self.assertEqual(user_dict['password'], "password123")
        self.assertIn('first_name', user_dict)
        self.assertIsInstance(user_dict['first_name'], str)
        self.assertEqual(user_dict['first_name'], "John")
        self.assertIn('last_name', user_dict)
        self.assertIsInstance(user_dict['last_name'], str)
        self.assertEqual(user_dict['last_name'], "Doe")

if __name__ == '__main__':
    unittest.main()
