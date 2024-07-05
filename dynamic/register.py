#!/usr/bin/python3
""" Starts a Flash Web Application """

from models import storage
from models.user import User
from os import environ
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import Flask
from werkzeug.security import generate_password_hash
from flask_login import login_user, current_user
from sqlalchemy import or_
  
app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        full_name = request.form.get('full_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = storage.all(User).filter(or_(User.email == "email",
                                             User.phone == "phone")).first()
        if user:
            flash('Email/Phone already exists.', category='error')
        elif len(email) < 4 or len(phone) != (10 or 15):
            flash('Email/Phone must be > 3/10 or 15 chars', category='error')
        elif len(full_name) < 5:
            flash('Full_name must be greater than 4 char.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 4:
            flash('Password must be at least 5 characters.', category='error')
        else:
            new_user = User(email=email, phone=phone, full_name=full_name,
                            password=generate_password_hash(password1, method='sha256'))
            storage.new(new_user)
            storage.save()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('templates.vehicle'))

    return render_template("register.html", user=current_user)
    
if __name__ == "__main__":
    """Register Function """
    app.run(host='0.0.0.0', port=5000)