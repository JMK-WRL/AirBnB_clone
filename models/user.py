#!/usr/bin/python3
"""Module that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    __name__ = "User"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
