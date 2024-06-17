#!/usr/bin/python3
"""This module defines the shipment class of Easy Freieght"""

from datetime import datetime

class Shipment(BaseModel):
    """
    Represents a shipment in the system with various attributes.
    Inherits from BaseModel for common attributes and methods.
    """

    id = str  # Shipment ID (primary key)
    user_id = str  # User ID (foreign key references User.id)
    origin = str  # Origin (address)
    destination = str  # Destination (address)
    cargo_type = str  # Cargo Type
    weight = float  # Weight
    description = str  # Description
    desired_price = float  # Desired Price
    status = str  # Status (Open/Quoted/Booked/Completed/Cancelled)
    created_at = datetime  # Creation Date

    def __init__(self, *args, **kwargs):
        """
        Initializes a Shipment instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing shipment attributes.
        """
        super().__init__(*args, **kwargs)
