#!/usr/bin/python3
""" This module defines the User class of Easy Freight"""

from datetime import datetime
import uuid
from passlib.hash import bcrypt  # Secure password hashing

class User(BaseModel):
    """
    Represents a user entity within the Easy Freight website.

    Attributes:
        full_name (str): The user's full name.
        email (str): The user's email address.
        phone_number (str): The user's phone number.
        password (str): The user's hashed password (stored securely).
        is_carrier (bool): Whether the user is a carrier (True) or a customer (False).
        business_license (str, optional): The carrier's business license number (if applicable).
        truck_plate_number (str, optional): The carrier's truck plate number (if applicable).
        id (str): Unique identifier for the user (generated automatically).
        created_at (datetime): Timestamp of user creation.
        updated_at (datetime): Timestamp of last user update.
    """

    full_name = str
    email = str
    phone_number = str
    password = str
    is_carrier = bool
    business_license = str  # Optional, only for carriers
    truck_plate_number = str  # Optional, only for carriers

    def __init__(self, *args, **kwargs):
        """
        Initializes a User instance.

        Args:
            *args: Positional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments passed to the BaseModel constructor.

        If no ID is provided, a unique ID is generated using uuid.uuid4().
        Sets the created_at and updated_at timestamps to the current datetime.
        """

        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def set_password(self, password):
        """
        Sets the user's password securely using bcrypt hashing.

        Args:
            password (str): The user's plain text password.
        """

        self.password = bcrypt.hash(password)  # Hash password securely

    def verify_password(self, password):
        """
        Verifies the user's password using bcrypt comparison.

        Args:
            password (str): The plain text password to compare.

        Returns:
            bool: True if the password matches, False otherwise.
        """

        return bcrypt.verify(password, self.password)  # Securely compare passwords
