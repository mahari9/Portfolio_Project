#!/usr/bin/python3
""" objects that handle all default RestFul API actions for carriers"""
from models.carrier import Carrier
from models import storage
from api.v1.views import create_app
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@create_app.route('/carriers', methods=['GET'], strict_slashes=False)
@swag_from('documentation/carrier/get_carrier.yml', methods=['GET'])
def get_carriers():
    """
    Retrieves the list of all carrier objects
    """
    all_carriers = storage.all(Carrier).values()
    list_carriers = []
    for carrier in all_carriers:
        list_carriers.append(carrier.to_dict())
    return jsonify(list_carriers)


@create_app.route('/carriers/<carrier_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/carrier/get_id_carrier.yml', methods=['get'])
def get_carrier(carrier_id):
    """ Retrieves a specific carrier """
    carrier = storage.get(Carrier, carrier_id)
    if not carrier:
        abort(404)

    return jsonify(carrier.to_dict())


@create_app.route('/carriers/<carrier_id>', methods=['DELETE'],
                strict_slashes=False)
@swag_from('documentation/carrier/delete_carrier.yml', methods=['DELETE'])
def delete_carrier(carrier_id):
    """
    Deletes a carrier Object
    """

    carrier = storage.get(Carrier, carrier_id)

    if not carrier:
        abort(404)

    storage.delete(carrier)
    storage.save()

    return make_response(jsonify({}), 200)


@create_app.route('/carriers', methods=['POST'], strict_slashes=False)
@swag_from('documentation/carrier/post_carrier.yml', methods=['POST'])
def post_carrier():
    """
    Creates a carrier
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Carrier(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@create_app.route('/carriers/<carrer_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/carrier/put_carrier.yml', methods=['PUT'])
def put_carrier(carrier_id):
    """
    Updates a carrier object
    """
    carrier = storage.get(Carrier, carrier_id)

    if not carrier:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(carrier, key, value)
    storage.save()
    return make_response(jsonify(carrier.to_dict()), 200)