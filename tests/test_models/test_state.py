#!/usr/bin/python3


import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_instance(self):
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_str(self):
        expected_output = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_output)

    def test_save(self):
        original_updated_at = self.state.updated_at
        self.state.save()
        new_updated_at = self.state.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

        new_state = State()
        new_state.save()
        with open('file.json', 'r') as file:
            self.assertIn("State." + new_state.id, file.read())

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["id"], self.state.id)
        self.assertEqual(state_dict["created_at"],
                         self.state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"],
                         self.state.updated_at.isoformat())
