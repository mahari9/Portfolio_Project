#!/usr/bin/python3
"""This module defines the vehicle class for Easy Freight"""

from base_model import BaseModel
from user import User

class Vehicle(BaseModel):
    """
    Represents a carrier's vehicle with various attributes.
    Inherits from BaseModel for common attributes and methods.
    """
    
    
    vehicle_id = str # Unique identifier for the vehicle, primary key    
    carrier_id = str # Identifier of the carrier who owns this vehicle, foreign key    
    model = str # Model of the vehicle    
    capacity = float # Capacity of the vehicle in terms of weight it can carry
    plate_number = str  # License plate number of the vehicle
    colour = str  # Color of the vehicle
    
   def __init__(self, *args, **kwargs):
        """
        Initializes an vehicle instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing vehicle attributes.
        """
        super().__init__(*args, **kwargs)
