#!/usr/bin/python3

from user import User

def register_user(name, email, phone_number, password, password_verify, is_carrier, business_license="", truck_plate_number=""):
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
    # Implement database interaction to find the user (replace with your database code)
    # user = find_user_by_username(username)

    if not user:
        raise ValueError("Invalid username")

    if not user.verify_password(password):
        raise ValueError("Invalid password")

    # Set session information here (replace with your session management approach)
    # set_user_session(user)

    return user
