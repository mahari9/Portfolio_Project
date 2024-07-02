#!/usr/bin/python3
"""This module defines the vehicle class for Easy Freight"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, ForeignKey

class Vehicle(BaseModel, Base):
    """
    Represents a carrier's vehicle with various attributes.
    Inherits from BaseModel for common attributes and methods.
    """
    
    if models.storage_t == "db":
        __tablename__ = 'vehicles'
        vehicle_type = Column(String(128), nullable=False)
        carrier_id = Column(String(128), ForeignKey('carriers.id'), nullable=False)    
        model = Column(String(128), nullable=True)    
        cargo_capacity = Column(Float, nullable=False)
        plate_number = Column(String(128), nullable=False)
        color = Column(String(128), nullable=False)
        price_per_km = Column(Float, nullable=False)
        
    else:
        vehicle_type = ""
        carrier_id = ""
        model = ""
        cargo_capacity = 0.0
        plate_number = ""
        color = ""
        price_per_km = 0.0
        
    def __init__(self, *args, **kwargs):
        """
        Initializes an vehicle instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing vehicle attributes.
        """
        super().__init__(*args, **kwargs)
