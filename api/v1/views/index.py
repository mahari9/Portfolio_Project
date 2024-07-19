#!/usr/bin/python3
""" Index """
from models.user import User
from models.carrier import Carrier
from models.vehicle import Vehicle
from models import storage
from api.v1.views import create_app
from flask import jsonify


@create_app.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@create_app.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [User, Carrier, Vehicle]
    names = ["users", "carriers", "vehicles"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)