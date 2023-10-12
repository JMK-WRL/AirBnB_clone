#!/usr/bin/python3
"""Unittest for the user module"""


import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up a User instance for testing.
        """
        self.user = User()

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.user

    def test_email_attribute(self):
        """
        Test the 'email' attribute data type in User.
        """
        self.assertIsInstance(self.user.email, str)

    def test_email_default_value(self):
        """
        Test that the 'email' attribute has an empty string as its default value.
        """
        self.assertEqual(self.user.email, "")

    def test_email_assignment(self):
        """
        Test the assignment of a value to the 'email' attribute.
        """
        self.user.email = "user@example.com"
        self.assertEqual(self.user.email, "user@example.com")

    def test_password_attribute(self):
        """
        Test the 'password' attribute data type in User.
        """
        self.assertIsInstance(self.user.password, str)

    def test_password_default_value(self):
        """
        Test that the 'password' attribute has an empty string as its default value.
        """
        self.assertEqual(self.user.password, "")

    def test_password_assignment(self):
        """
        Test the assignment of a value to the 'password' attribute.
        """
        self.user.password = "password123"
        self.assertEqual(self.user.password, "password123")

    def test_first_name_attribute(self):
        """
        Test the 'first_name' attribute data type in User.
        """
        self.assertIsInstance(self.user.first_name, str)

    def test_first_name_default_value(self):
        """
        Test that the 'first_name' attribute has an empty string as its default value.
        """
        self.assertEqual(self.user.first_name, "")

    def test_first_name_assignment(self):
        """
        Test the assignment of a value to the 'first_name' attribute.
        """
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_last_name_attribute(self):
        """
        Test the 'last_name' attribute data type in User.
        """
        self.assertIsInstance(self.user.last_name, str)

    def test_last_name_default_value(self):
        """
        Test that the 'last_name' attribute has an empty string as its default value.
        """
        self.assertEqual(self.user.last_name, "")

    def test_last_name_assignment(self):
        """
        Test the assignment of a value to the 'last_name' attribute.
        """
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")

    def test_inheritance(self):
        """
        Test that the User class inherits from BaseModel.
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_to_dict(self):
        """
        Test the 'to_dict' method in User.
        """
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)

    def test_to_dict_id_type(self):
        """
        Test the data type of the 'id' attribute in the 'to_dict' output.
        """
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict['id'], str)

    def test_to_dict_created_at_type(self):
        """
        Test the data type of the 'created_at' attribute in the 'to_dict' output.
        """
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict['created_at'], str)

    def test_to_dict_updated_at_type(self):
        """
        Test the data type of the 'updated_at' attribute in the 'to_dict' output.
        """
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
