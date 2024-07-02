#!/usr/bin/python3
""" This module defines the registration/login for Easy Freight"""

import models
from models.user import User

# Import a session management library (example using Flask-Session)
from flask import session

def register_user(name, email, phone_number, password, password_verify, is_carrier, business_license="", truck_plate_number=""):
    """
    Registers a new user and returns a User object.

    Args:
        name (str): The user's full name.
        email (str): The user's email address.
        phone_number (str): The user's phone number.
        password (str): The user's plain text password.
        password_verify (str): The user's password confirmation.
        is_carrier (bool): Whether the user is a carrier (True) or a customer (False).
        business_license (str, optional): The carrier's business license number (if applicable).
        truck_plate_number (str, optional): The carrier's truck plate number (if applicable).

    Raises:
        ValueError: If passwords do not match.

    Returns:
        User: An instance of the User class representing the newly registered user.
    """

    if password != password_verify:
        raise ValueError("Passwords do not match")

    user = User(name=name, email=email, phone_number=phone_number, is_carrier=is_carrier)
    user.set_password(password)

    if is_carrier:
        user.business_license = business_license
        user.truck_plate_number = truck_plate_number

    # Implement database interaction to save the user (replace with your database code)
    # save_user(user)

    return user


def login_user(username, password):
    """
    Attempts to log in a user and returns a User object on success.

    Args:
        username (str): The user's username for login.
        password (str): The user's plain text password.

    Raises:
        ValueError: If username or password is invalid.

    Returns:
        User: An instance of the User class representing the logged-in user.
    """

    # Implement database interaction to find the user (replace with your database code)
    # user = find_user_by_username(username)

    if not user:
        raise ValueError("Invalid username")

    if not user.verify_password(password):
        raise ValueError("Invalid password")

    # Set session information here (using Flask-Session)
    session['user_id'] = user.id
    return user
