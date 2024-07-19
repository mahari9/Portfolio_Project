#!/usr/bin/python3
""" Starts a Flash Web Application """

from models import storage
from models.user import User
from os import environ
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import Flask
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import or_

app = Flask(__name__)

# Create a blueprint for login-related routes
login_bp = Blueprint('login', __name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and ('email' in request.form or 'phone' in request.form) and 'password' in request.form:
        try:
            # Query for filtering
            user = storage.all(User).filter(or_(User.email == request.form['email'], User.phone == request.form['phone'])).first()
            if user:
                if check_password_hash(user.password, request.form['password']):
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('templates.vehicle'))
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
                flash('Email address not found.', category='warning')
        except Exception as e:
            flash(f"An error occurred: {str(e)}", category='error')
        return render_template("login.html", user=current_user)

    return render_template("login.html", user=current_user)  # Display login form for GET requests

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
