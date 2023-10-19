#!/usr/bin/python3
"""this script is the base model"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs is not None and kwargs != {}:
            # If keyword arguments (kwargs) are provided during initialization
            for key in kwargs:
                if key == "created_at":
                    # If "created_at" key is found, parse it as a datetime
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    # If "updated_at" key is found, parse it as a datetime
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    # For other keys, assign their values to the instance
                    self.__dict__[key] = kwargs[key]
        else:
            # If no kwargs provided, initialize default attributes
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = datetime.now()  # Current date and time
            self.updated_at = datetime.now()  # Current date and time
            storage.new(self)  # Add the instance to the storage

    def __str__(self):
        """Returns official string representation"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()  # Update the 'updated_at' attribute
        storage.save()  # Save the updated instance to storage

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()  # Copy the instance's dictionary
        my_dict["__class__"] = type(self).__name__  # Add class name
        my_dict["created_at"] = my_dict["created_at"].isoformat()  # Format datetime
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()  # Format datetime
        return my_dict
