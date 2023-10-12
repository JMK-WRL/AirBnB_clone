#!/usr/bin/python3
"""Unittest for the Amenity file."""

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage

class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up an Amenity instance for testing.
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.amenity

    def test_name_attribute(self):
        """
        Test the 'name' attribute data type in Amenity.
        """
        self.assertIsInstance(self.amenity.name, str)

    def test_name_default_value(self):
        """
        Test that the 'name' attribute has an empty string as its default value.
        """
        self.assertEqual(self.amenity.name, "")

    def test_name_assignment(self):
        """
        Test the assignment of a value to the 'name' attribute.
        """
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_inheritance(self):
        """
        Test that the Amenity class inherits from BaseModel.
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_to_dict(self):
        """
        Test the 'to_dict' method in Amenity.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)

    def test_to_dict_id_type(self):
        """
        Test the data type of the 'id' attribute in the 'to_dict' output.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict['id'], str)

    def test_to_dict_created_at_type(self):
        """
        Test the data type of the 'created_at' attribute in the 'to_dict' output.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict['created_at'], str)

    def test_to_dict_updated_at_type(self):
        """
        Test the data type of the 'updated_at' attribute in the 'to_dict' output.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
