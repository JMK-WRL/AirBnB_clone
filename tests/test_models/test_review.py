#!/usr/bin/python3
"""Unittest for the review module."""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up a Review instance for testing.
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.review

    def test_place_id_attribute(self):
        """
        Test the 'place_id' attribute data type in Review.
        """
        self.assertIsInstance(self.review.place_id, str)

    def test_place_id_default_value(self):
        """
        Test that the 'place_id' attribute has an empty string as its default value.
        """
        self.assertEqual(self.review.place_id, "")

    def test_place_id_assignment(self):
        """
        Test the assignment of a value to the 'place_id' attribute.
        """
        self.review.place_id = "12345"
        self.assertEqual(self.review.place_id, "12345")

    def test_user_id_attribute(self):
        """
        Test the 'user_id' attribute data type in Review.
        """
        self.assertIsInstance(self.review.user_id, str)

    def test_user_id_default_value(self):
        """
        Test that the 'user_id' attribute has an empty string as its default value.
        """
        self.assertEqual(self.review.user_id, "")

    def test_user_id_assignment(self):
        """
        Test the assignment of a value to the 'user_id' attribute.
        """
        self.review.user_id = "67890"
        self.assertEqual(self.review.user_id, "67890")

    def test_text_attribute(self):
        """
        Test the 'text' attribute data type in Review.
        """
        self.assertIsInstance(self.review.text, str)

    def test_text_default_value(self):
        """
        Test that the 'text' attribute has an empty string as its default value.
        """
        self.assertEqual(self.review.text, "")

    def test_text_assignment(self):
        """
        Test the assignment of a value to the 'text' attribute.
        """
        self.review.text = "A wonderful place to stay!"
        self.assertEqual(self.review.text, "A wonderful place to stay!")

    def test_inheritance(self):
        """
        Test that the Review class inherits from BaseModel.
        """
        self.assertIsInstance(self.review, BaseModel)

    def test_to_dict(self):
        """
        Test the 'to_dict' method in Review.
        """
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)

    def test_to_dict_id_type(self):
        """
        Test the data type of the 'id' attribute in the 'to_dict' output.
        """
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict['id'], str)

    def test_to_dict_created_at_type(self):
        """
        Test the data type of the 'created_at' attribute in the 'to_dict' output.
        """
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict['created_at'], str)

    def test_to_dict_updated_at_type(self):
        """
        Test the data type of the 'updated_at' attribute in the 'to_dict' output.
        """
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
