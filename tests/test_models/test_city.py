#!/usr/bin/python3
"""Uniitest for city module"""


import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up a City instance for testing.
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.city

    def test_state_id_attribute(self):
        """
        Test the 'state_id' attribute data type in City.
        """
        self.assertIsInstance(self.city.state_id, str)

    def test_state_id_default_value(self):
        """
        Test that the 'state_id' attribute has an empty string as its default value.
        """
        self.assertEqual(self.city.state_id, "")

    def test_state_id_assignment(self):
        """
        Test the assignment of a value to the 'state_id' attribute.
        """
        self.city.state_id = "TX"
        self.assertEqual(self.city.state_id, "TX")

    def test_name_attribute(self):
        """
        Test the 'name' attribute data type in City.
        """
        self.assertIsInstance(self.city.name, str)

    def test_name_default_value(self):
        """
        Test that the 'name' attribute has an empty string as its default value.
        """
        self.assertEqual(self.city.name, "")

    def test_name_assignment(self):
        """
        Test the assignment of a value to the 'name' attribute.
        """
        self.city.name = "Austin"
        self.assertEqual(self.city.name, "Austin")

    def test_inheritance(self):
        """
        Test that the City class inherits from BaseModel.
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_to_dict(self):
        """
        Test the 'to_dict' method in City.
        """
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)

    def test_to_dict_id_type(self):
        """
        Test the data type of the 'id' attribute in the 'to_dict' output.
        """
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict['id'], str)

    def test_to_dict_created_at_type(self):
        """
        Test the data type of the 'created_at' attribute in the 'to_dict' output.
        """
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict['created_at'], str)

    def test_to_dict_updated_at_type(self):
        """
        Test the data type of the 'updated_at' attribute in the 'to_dict' output.
        """
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
