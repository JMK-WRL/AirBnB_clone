#!/usr/bin/python3
"""Uniitest for the BaseModel class."""


import unittest
from models.base_model import BaseModel
import datetime
import json
import os

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Create an instance of BaseModel for testing
        self.base_model = BaseModel()

    def tearDown(self):
        # Clean up after each test
        del self.base_model

    def test_id_type(self):
        """Test the data type of the 'id' attribute in BaseModel."""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        """Test the data type of the 'created_at' attribute in BaseModel."""
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """Test the data type of the 'updated_at' attribute in BaseModel."""
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_to_dict_type(self):
        """Test the data type of the 'to_dict' method's return value in BaseModel."""
        self.assertIsInstance(self.base_model.to_dict(), dict)

    def test_str_output(self):
        """Test the string representation of BaseModel."""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        """Test the 'save' method in BaseModel."""
        self.base_model.save()
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_create_instance_with_dict(self):
        """Test creating a BaseModel instance from a dictionary representation."""
        base_model_dict = self.base_model.to_dict()
        new_base_model = BaseModel(**base_model_dict)
        self.assertEqual(self.base_model.id, new_base_model.id)
        self.assertEqual(self.base_model.created_at, new_base_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_base_model.updated_at)

    def test_create_instance_with_dict_custom_time_format(self):
        """Test creating a BaseModel instance from a dictionary with custom time format."""
        base_model_dict = self.base_model.to_dict()
        new_base_model = BaseModel(**base_model_dict)
        self.assertEqual(self.base_model.id, new_base_model.id)
        self.assertEqual(self.base_model.created_at, new_base_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_base_model.updated_at)

if __name__ == '__main__':
    unittest.main()
