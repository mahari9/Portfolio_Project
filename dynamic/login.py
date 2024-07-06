#!/usr/bin/python3
"""Starts the flask web aplication"""

from models import storage
from models.user import User
from os import environ
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import Flask
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import or_

  
app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def Login():
    if request.method == 'POST' and ('email' in request.form or 'phone' in request.form) and 'password' in request.form:
        if 'email' in request.form:
            email = request.form['email']
            login_field = 'email'  # Track which field was used for login attempt
        else:
            phone = request.form['phone']
            login_field = 'phone'
        password = request.form['password']

        user = storage.all(User).filter(or_(User.email == "email",
                                             User.phone == "phone")).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('templates.vehicle'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.Login'))


if __name__ == "__main__":
    """ login Function """
    app.run(host='0.0.0.0', port=5000)