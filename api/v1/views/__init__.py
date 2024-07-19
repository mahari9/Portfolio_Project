#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

create_app = Blueprint('create_app', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.carriers import *
from api.v1.views.vehicles_carrier import *