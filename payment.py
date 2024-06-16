#!/usr/bin/python3
"""This module defines the payment class for Easy Freight"""

from sqlalchemy import Integer, DateTime
from base_model import BaseModel
from user import User
from shipment import Shipment

class Payment(BaseModel):
    """
    Represents a payment transaction in the system with various attributes.
    Inherits from BaseModel for common attributes and methods.
    """
        
    payment_id = str # Unique identifier for the payment, primary key    
    user_id = str # Identifier of the user making the payment, foreign key    
    shipment_id = str # Identifier of the shipment associated with this payment, foreign key
    amount = Intger # Amount paid for the shipment
    payment_method = str # Method used for payment    
    payment_date = (DateTime # Date when the payment was made

   
   def __init__(self, *args, **kwargs):
        """
        Initializes an payment instance.

        Args:
            *args: Variable-length argument list (unused in this case).
            **kwargs: Keyword argument dictionary containing payment attributes.
        """
        super().__init__(*args, **kwargs)
