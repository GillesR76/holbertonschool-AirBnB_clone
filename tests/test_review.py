#!/usr/bin/python3


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_instance(self):
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str(self):
        expected_output = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_output)

    def test_save(self):
        original_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

        new_review = Review()
        new_review.save()
        with open('file.json', 'r') as file:
            self.assertIn("Review." + new_review.id, file.read())

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["id"], self.review.id)
        self.assertEqual(review_dict["created_at"],
                         self.review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"],
                         self.review.updated_at.isoformat())
