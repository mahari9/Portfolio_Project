#!/usr/bin/python3
"""This module defines the shipment class of Easy Freieght"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Shipment(BaseModel, Base):
    """
    Represents a shipment in the system with various attributes.
    Inherits from BaseModel for common attributes and methods.
    """
   
    if models.storage_t == 'db':
        __tablename__ = 'places'
        shipper_id = Column(String(60), ForeignKey('shipper_id'), nullable=False)
        origin = Column(String(128), nullable=False)
        destination = Column(String(128), nullable=False)
        cargo_type = Column(String(128), nullable=False)
        weight = Column(float, nullable=False)
        description = Column(String(1024), nullable=True)
        desired_vehicle = Column(String(128), nullable=True)
        status = Column(String(128), nullable=False) # Status (Open/Quoted/Booked/Completed/Cancelled)
        carrier_id = Column(String(60), ForeignKey('carrier_id'), nullable=True)
        offers = relationship("Offer",
                               backref="Shipment",
                               cascade="all, delete, delete-orphan")
       

    else:
        shipper_id = ""
        origin = ""
        destination = ""
        cargo_type = ""
        weight = 0.0
        description = ""
        desired_vehicle = ""
        status = ""
        carrier_id = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a Shipment instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing shipment attributes.
        """
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def offers(self):
            """getter attribute returns the list of Offer instances"""
            from models.offer import Offer
            offer_list = []
            all_offers = models.storage.all(Offer)
            for offer in all_offers.values():
                if offer.shipment_id == self.id:
                    offer_list.append(offer)
            return offer_list
