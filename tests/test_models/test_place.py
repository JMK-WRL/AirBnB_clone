#!/usr/bin/python3
"""Unittest for place module"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up a Place instance for testing.
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.place

    def test_city_id_attribute(self):
        """
        Test the 'city_id' attribute data type in Place.
        """
        self.assertIsInstance(self.place.city_id, str)

    def test_city_id_default_value(self):
        """
        Test that the 'city_id' attribute has an empty string as its default value.
        """
        self.assertEqual(self.place.city_id, "")

    def test_city_id_assignment(self):
        """
        Test the assignment of a value to the 'city_id' attribute.
        """
        self.place.city_id = "NYC"
        self.assertEqual(self.place.city_id, "NYC")

    def test_user_id_attribute(self):
        """
        Test the 'user_id' attribute data type in Place.
        """
        self.assertIsInstance(self.place.user_id, str)

    def test_user_id_default_value(self):
        """
        Test that the 'user_id' attribute has an empty string as its default value.
        """
        self.assertEqual(self.place.user_id, "")

    def test_user_id_assignment(self):
        """
        Test the assignment of a value to the 'user_id' attribute.
        """
        self.place.user_id = "12345"
        self.assertEqual(self.place.user_id, "12345")

    def test_name_attribute(self):
        """
        Test the 'name' attribute data type in Place.
        """
        self.assertIsInstance(self.place.name, str)

    def test_name_default_value(self):
        """
        Test that the 'name' attribute has an empty string as its default value.
        """
        self.assertEqual(self.place.name, "")

    def test_name_assignment(self):
        """
        Test the assignment of a value to the 'name' attribute.
        """
        self.place.name = "Cozy Cottage"
        self.assertEqual(self.place.name, "Cozy Cottage")

    def test_description_attribute(self):
        """
        Test the 'description' attribute data type in Place.
        """
        self.assertIsInstance(self.place.description, str)

    def test_description_default_value(self):
        """
        Test that the 'description' attribute has an empty string as its default value.
        """
        self.assertEqual(self.place.description, "")

    def test_description_assignment(self):
        """
        Test the assignment of a value to the 'description' attribute.
        """
        self.place.description = "A beautiful place by the sea"
        self.assertEqual(self.place.description, "A beautiful place by the sea")

    def test_number_rooms_attribute(self):
        """
        Test the 'number_rooms' attribute data type in Place.
        """
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_rooms_default_value(self):
        """
        Test that the 'number_rooms' attribute has 0 as its default value.
        """
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_rooms_assignment(self):
        """
        Test the assignment of a value to the 'number_rooms' attribute.
        """
        self.place.number_rooms = 3
        self.assertEqual(self.place.number_rooms, 3)

    def test_number_bathrooms_attribute(self):
        """
        Test the 'number_bathrooms' attribute data type in Place.
        """
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_number_bathrooms_default_value(self):
        """
        Test that the 'number_bathrooms' attribute has 0 as its default value.
        """
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_number_bathrooms_assignment(self):
        """
        Test the assignment of a value to the 'number_bathrooms' attribute.
        """
        self.place.number_bathrooms = 2
        self.assertEqual(self.place.number_bathrooms, 2)

    def test_max_guest_attribute(self):
        """
        Test the 'max_guest' attribute data type in Place.
        """
        self.assertIsInstance(self.place.max_guest, int)

    def test_max_guest_default_value(self):
        """
        Test that the 'max_guest' attribute has 0 as its default value.
        """
        self.assertEqual(self.place.max_guest, 0)

    def test_max_guest_assignment(self):
        """
        Test the assignment of a value to the 'max_guest' attribute.
        """
        self.place.max_guest = 4
        self.assertEqual(self.place.max_guest, 4)

    def test_price_by_night_attribute(self):
        """
        Test the 'price_by_night' attribute data type in Place.
        """
        self.assertIsInstance(self.place.price_by_night, int)

    def test_price_by_night_default_value(self):
        """
        Test that the 'price_by_night' attribute has 0 as its default value.
        """
        self.assertEqual(self.place.price_by_night, 0)

    def test_price_by_night_assignment(self):
        """
        Test the assignment of a value to the 'price_by_night' attribute.
        """
        self.place.price_by_night = 100
        self.assertEqual(self.place.price_by_night, 100)

    def test_latitude_attribute(self):
        """
        Test the 'latitude' attribute data type in Place.
        """
        self.assertIsInstance(self.place.latitude, float)

    def test_latitude_default_value(self):
        """
        Test that the 'latitude' attribute has 0.0 as its default value.
        """
        self.assertEqual(self.place.latitude, 0.0)

    def test_latitude_assignment(self):
        """
        Test the assignment of a value to the 'latitude' attribute.
        """
        self.place.latitude = 30.2672
        self.assertEqual(self.place.latitude, 30.2672)

    def test_longitude_attribute(self):
        """
        Test the 'longitude' attribute data type in Place.
        """
        self.assertIsInstance(self.place.longitude, float)

    def test_longitude_default_value(self):
        """
        Test that the 'longitude' attribute has 0.0 as its default value.
        """
        self.assertEqual(self.place.longitude, 0.0)

    def test_longitude_assignment(self):
        """
        Test the assignment of a value to the 'longitude' attribute.
        """
        self.place.longitude = -97.7431
        self.assertEqual(self.place.longitude, -97.7431)

    def test_amenity_ids_attribute(self):
        """
        Test the 'amenity_ids' attribute data type in Place.
        """
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_amenity_ids_default_value(self):
        """
        Test that the 'amenity_ids' attribute has an empty list as its default value.
        """
        self.assertEqual(self.place.amenity_ids, [])

    def test_amenity_ids_assignment(self):
        """
        Test the assignment of a value to the 'amenity_ids' attribute.
        """
        amenity_list = ["pool", "wifi", "gym"]
        self.place.amenity_ids = amenity_list
        self.assertEqual(self.place.amenity_ids, amenity_list)

    def test_inheritance(self):
        """
        Test that the Place class inherits from BaseModel.
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_to_dict(self):
        """
        Test the 'to_dict' method in Place.
        """
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)

    def test_to_dict_id_type(self):
        """
        Test the data type of the 'id' attribute in the 'to_dict' output.
        """
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict['id'], str)

    def test_to_dict_created_at_type(self):
        """
        Test the data type of the 'created_at' attribute in the 'to_dict' output.
        """
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict['created_at'], str)

    def test_to_dict_updated_at_type(self):
        """
        Test the data type of the 'updated_at' attribute in the 'to_dict' output.
        """
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
