#!/usr/bin/python3
"""This module defines the tracking class for Easy Freight"""

from base_model import BaseModel
from shipment import Shipment

class Tracking(BaseModel):
    """
    Represents tracking information for a shipment.
    Inherits from BaseModel for common attributes and methods.
    """    
    
    tracking_id = str # Unique identifier for the tracking record, primary key
    shipment_id = str # Identifier of the shipment being tracked, foreign key
    current_location = str # Current location of the shipment        
    status_updates = str # Status updates for the shipment        
    timestamps = DateTime # Timestamps for each status update
   
   def __init__(self, *args, **kwargs):
        """
        Initializes an tracking instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing tracking attributes.
        """
        super().__init__(*args, **kwargs)
