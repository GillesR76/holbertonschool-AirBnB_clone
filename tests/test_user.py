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

    def test_user_email(self):
        user = User()
        self.assertEqual(user.email, "")

    def test_user_email_1(self):
        user = User()
        user.email = "arsene@example.fr"
        self.assertEqual(user.email, "arsene@example.fr")

    def test_user_password(self):
        user = User()
        self.assertEqual(user.password, "")

    def test_user_password_1(self):
        user = User()
        user.password = "8956"
        self.assertEqual(user.password, "8956")

    def test_user_first_name(self):
        user = User()
        self.assertEqual(user.first_name, "")

    def test_user_first_name_1(self):
        user = User()
        user.first_name = "Arsene"
        self.assertEqual(user.first_name, "Arsene")

    def test_user_last_name(self):
        user = User()
        self.assertEqual(user.last_name, "")

    def test_user_last_name_1(self):
        user = User()
        user.last_name = "Giriteka"
        self.assertEqual(user.last_name, "Giriteka")


if __name__ == '__main__':
    unittest.main()
