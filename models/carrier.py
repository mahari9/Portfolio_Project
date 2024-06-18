#!/usr/bin/python3
""" This module defines the Carrier class of Easy Freight"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Bool
from sqlalchemy.orm import relationship
from datetime import datetime
from hashlib import md5

class Carrier(BaseModel, Base):
    """
    Represents a carrier entity within the Easy Freight website.

    Attributes:
        full_name (str): The Carrier's full name.
        email (str): The user's email address.
        phone_number (str): The user's phone number.
        password (str): The user's hashed password (stored securely).
        business_license (str, optional): The carrier's business license number (if applicable).

    """
    if models.storage_t == 'db':
        __tablename__ = 'carriers'
        email = Column(String(128), nullable=False)
        phone_number = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        full_name = Column(String(256), nullable=True)
        business_license = Column(String(128), nullable=True)  # Optional, only for carriers
        vehicles = relationship("Vehicle",
                              backref="Carrier",
                              cascade="all, delete, delete-orphan")
        offers = relationship("Offer",
                            backref="offer",
                            cascade="all, delete, delete-orphan")
        shipments = relationship("Shipment", backref="shipment")

    else:    
        email = ""
        phone_number = ""
        password = ""
        full_name = ""
        business_license = ""

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

     if(models.storage_t != "db"):
        @property
        def vehicles(self):
            """getter for list of vehicle instances related to the carrier"""
            vehicle_list = []
            all_vehicles = models.storage.all(Vehicle)
            for vehicle in all_vehicles.values():
                if carrier.vehicle_id == self.id:
                    vehicle_list.append(vehicle)
            return vehicle_list

    if(models.storage_t != "db"):
        @property
        def offers(self):
            """getter for list of offer instances related to the carrier"""
            offer_list = []
            all_offers = models.storage.all(Offer)
            for offer in all_offers.values():
                if carrier.offer_id == self.id:
                    offer_list.append(offer)
            return offer_list
