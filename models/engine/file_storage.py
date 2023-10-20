#!/usr/bin/python3
"""FileStorage Module."""
import datetime
import json
import os

class FileStorage:
    """Store and Retrieve Data."""
    __file_path = "file.json"  # Path to the data storage file
    __objects = {}  # Dictionary for storing objects

    def classes(self):
        """Return a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        # Dictionary of class names and their references
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes


    def all(self):
        """Return the stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add an object to the dictionary with a unique key."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to a JSON file (at __file_path)."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            # Serialize objects to a dictionary of dictionaries
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    
    def reload(self):
        """Load previously stored objects from a JSON file."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            # Deserialize objects and store them in __objects
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Define valid attributes and their data types for each class."""
        # Dictionary of valid attributes and their types for each class
        attributes = {
            "BaseModel": {"id": str, "created_at": datetime.datetime, "updated_at": datetime.datetime},
            "User": {"email": str, "password": str, "first_name": str, "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {"city_id": str, "user_id": str, "name": str, "description": str,
                      "number_rooms": int, "number_bathrooms": int, "max_guest": int, "price_by_night": int,
                      "latitude": float, "longitude": float, "amenity_ids": list},
            "Review": {"place_id": str, "user_id": str, "text": str}
        }
        return attributes
