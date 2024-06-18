#!/usr/bin/python3
"""This module defines the offer class for Easy Freight"""

from datetime import datetime
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table

class Offer(BaseModel, Base):
    """
    Represents an offer made by a carrier for a shipment.
    Inherits from BaseModel for common attributes and methods.
    """

    if models.storage_t == 'db':
        __tablename__ = 'offers'
        shipment_id = Column(String(60), ForeignKey('shipment_id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        price = Column(Float, nullable=False)
        estimated_delivery_time = Column(Integer, nullable=False)
        submitted_at = Column(datetime, nullable=False)

    else:
        id = ""  # Offer ID (primary key)
        shipment_id = ""  # Shipment ID (foreign key references Shipment.id)
        carrier_id = ""  # Carrier ID (foreign key references User.id)
        price = 0.0  # Price offered by the carrier
        estimated_delivery_time = 0  # Estimated delivery time in days
        submitted_at = ""  # Submission Date

    def __init__(self, *args, **kwargs):
        """
        Initializes an Offer instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing offer attributes.
        """
        super().__init__(*args, **kwargs)
