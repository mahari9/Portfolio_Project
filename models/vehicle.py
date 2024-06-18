#!/usr/bin/python3
"""This module defines the vehicle class for Easy Freight"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Vehicle(BaseModel, Base):
    """
    Represents a carrier's vehicle with various attributes.
    Inherits from BaseModel for common attributes and methods.
    """
    
    if models.storage_t == "db":
        __tablename__ = 'vehicles'
        name = Column(String(128), nullable=False)
        carrier_id = Column(String(128), nullable=False)    
        model = Column(String(128), nullable=True)    
        capacity = Column(Float, nullable=False)
        plate_number = Column(String(128), nullable=False)
        colour = Column(String(128), nullable=False)
        offers = relationship("Offer", backref="offer")
        
    else:
        name = ""
        carrrier_id = "" 
        model = ""    
        capacity = 0.0
        plate_number = ""
        colour = ""
    
   def __init__(self, *args, **kwargs):
        """
        Initializes an vehicle instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing vehicle attributes.
        """
        super().__init__(*args, **kwargs)
