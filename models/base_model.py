#!/usr/bin/python3
"""This script is the base_model for the airbnb console"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:

    """Class to be inherited by all class models"""
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance.

        Args:
            args: list of arguments
            kwargs: dict of key-values arguments

        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        """self.updated_at = datetime.now()"""
        """Call save() method of storage"""
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data