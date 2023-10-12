#!/usr/bin/python3
"""Unittest for state module."""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up a State instance for testing.
        """
        self.state = State()

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.state

    def test_name_attribute(self):
        """
        Test the 'name' attribute data type in State.
        """
        self.assertIsInstance(self.state.name, str)

    def test_name_default_value(self):
        """
        Test that the 'name' attribute has an empty string as its default value.
        """
        self.assertEqual(self.state.name, "")

    def test_name_assignment(self):
        """
        Test the assignment of a value to the 'name' attribute.
        """
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_inheritance(self):
        """
        Test that the State class inherits from BaseModel.
        """
        self.assertIsInstance(self.state, BaseModel)

    def test_to_dict(self):
        """
        Test the 'to_dict' method in State.
        """
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_to_dict_id_type(self):
        """
        Test the data type of the 'id' attribute in the 'to_dict' output.
        """
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict['id'], str)

    def test_to_dict_created_at_type(self):
        """
        Test the data type of the 'created_at' attribute in the 'to_dict' output.
        """
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict['created_at'], str)

    def test_to_dict_updated_at_type(self):
        """
        Test the data type of the 'updated_at' attribute in the 'to_dict' output.
        """
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
