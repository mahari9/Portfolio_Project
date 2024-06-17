#!/usr/bin/python3
"""This module defines the offer class for Easy Freight"""

from datetime import datetime

class Offer(BaseModel):
    """
    Represents an offer made by a carrier for a shipment.
    Inherits from BaseModel for common attributes and methods.
    """

    id = str  # Offer ID (primary key)
    shipment_id = str  # Shipment ID (foreign key references Shipment.id)
    carrier_id = str  # Carrier ID (foreign key references User.id)
    price = float  # Price offered by the carrier
    estimated_delivery_time = int  # Estimated delivery time in days
    submitted_at = datetime  # Submission Date

    def __init__(self, *args, **kwargs):
        """
        Initializes an Offer instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing offer attributes.
        """
        super().__init__(*args, **kwargs)
