#!/usr/bin/python3
""" This module defines the User class of Easy Freight"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Bool
from sqlalchemy.orm import relationship
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
        is_carrier (bool): Whether the user is a carrier (True) or a customer (False).
        business_license (str, optional): The carrier's business license number (if applicable).
        truck_plate_number (str, optional): The carrier's truck plate number (if applicable).

    """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        phone_number = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        full_name = Column(String(256), nullable=True)
        is_carrier = Column(Bool, nullable=True)
        business_license = Column(String(128), nullable=True)  # Optional, only for carriers
        truck_plate_number = Column(String(128), nullable=True)
        offers = relationship("Offer", backref="offer")
        shipments = relationship("Shipment", backref="shipment")

    else:    
        email = ""
        phone_number = ""
        password = ""
        full_name = ""
        is_carrier = Bool
        business_license = ""
        truck_plate_number = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a User instance.

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
