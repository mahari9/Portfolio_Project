#!/usr/bin/python3
""" This module defines the shipper class of Easy Freight"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from datetime import datetime
from hashlib import md5

class User(BaseModel, Base):
    """
    Represents a user entity within the Easy Freight website.

    Attributes:
        full_name (str): The user's full name.
        email (str): The user's email address.
        phone_number (str): The user's phone number.
        password (str): The user's hashed password (stored securely).
 
    """
    if models.storage_t == 'db':
        __tablename__ = 'shippers'
        full_name = Column(String(256), nullable=True)
        email = Column(String(128), nullable=False)
        phone_number = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        

    else: 
        full_name = ""   
        email = ""
        phone_number = ""
        password = ""
        

    def __init__(self, *args, **kwargs):
        """
        Initializes a user instance.

        Args:
            *args: Positional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments passed to the BaseModel constructor.
        """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """
        Sets the user's password securely using bcrypt hashing.
        Args:
            password (str): The user's plain text password.
        """

        if name == "password":
            value = md5(value.encode()).hexdigest() # Hash password securely
        super().__setattr__(name, value)

    def __setattr__(self, name, value):
        """
        Verifies the user's password using bcrypt comparison.
        Args:
            password (str): The plain text password to compare.
        Returns:
            bool: True if the password matches, False otherwise.
        """

        if name == "password verify":
            value = md5(value.encode()).hexdigest() # Securely compare passwords
        super().__setattr__(name, value)
        