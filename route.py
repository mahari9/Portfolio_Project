#!/usr/bin/python3

"""This module defines the route class for Easy Freight"""

from sqlalchemy import String, Integer
from base_model import BaseModel


class Route(BaseModel):
    """
    Represents a shipping route in the system with various attributes.
    Inherits from BaseModel for common attributes and methods.
    """
    
    route_id = str # Unique identifier for the route, primary key    
    origin = str # Address of origin for the route
    destination = str # Destination address for the route 
    estimated_transit_time = Integer # Estimated transit time in hours

   
   def __init__(self, *args, **kwargs):
        """
        Initializes an route instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing route attributes.
        """
        super().__init__(*args, **kwargs)
