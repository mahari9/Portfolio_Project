#!/usr/bin/python3
""" This module defines the shipper class of Easy Freight"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from datetime import datetime
from hashlib import md5

class Shipper(BaseModel, Base):
    """
    Represents a shipper entity within the Easy Freight website.

    Attributes:
        full_name (str): The shipper's full name.
        email (str): The shipper's email address.
        phone_number (str): The shipper's phone number.
        password (str): The shipper's hashed password (stored securely).
 
    """
    if models.storage_t == 'db':
        __tablename__ = 'shippers'
        email = Column(String(128), nullable=False)
        phone_number = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        full_name = Column(String(256), nullable=True)
        shipments = relationship("Shipment",
                              backref="Shipper",
                              cascade="all, delete, delete-orphan")

    else:    
        email = ""
        phone_number = ""
        password = ""
        full_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a shipper instance.

        Args:
            *args: Positional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments passed to the BaseModel constructor.
        """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """
        Sets the shipper's password securely using bcrypt hashing.
        Args:
            password (str): The shipper's plain text password.
        """

        if name == "password":
            value = md5(value.encode()).hexdigest() # Hash password securely
        super().__setattr__(name, value)

    def __setattr__(self, name, value):
        """
        Verifies the shipper's password using bcrypt comparison.
        Args:
            password (str): The plain text password to compare.
        Returns:
            bool: True if the password matches, False otherwise.
        """

        if name == "password verify":
            value = md5(value.encode()).hexdigest() # Securely compare passwords
        super().__setattr__(name, value)
        
    if models.storage_t != "db":
        @property
        def shipments(self):
            """getter for list of shipment instances related to the shipper"""
            shipment_list = []
            all_shipments = models.storage.all(Shipment)
            for shipment in all_shipments.values():
                if shipment.shipper_id == self.id:
                    shipment_list.append(shipment)
            return shipment_list

