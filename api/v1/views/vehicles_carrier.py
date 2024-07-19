#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Vehicles """
from models.vehicle import Vehicle
from models.carrier import Carrier
from models import storage
from api.v1.views import create_app
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@create_app.route('/carriers/<carrier_id>/vehicles', methods=['GET'],
                strict_slashes=False)
@swag_from('documentation/vehicles/get_vehicles.yml', methods=['GET'])
def get_vehicles(carrier_id):
    """
    Retrieves the list of all vehicles objects of a carrier
    """
    carrier = storage.get(Carrier, carrier_id)

    if not carrier:
        abort(404)

    vehicles = [vehicle.to_dict() for vehicle in carrier.vehicles]

    return jsonify(vehicles)


@create_app.route('/vehicles/<vehicle_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/vehicles/get_vehicle.yml', methods=['GET'])
def get_vehicle(vehicle_id):
    """
    Retrieves a vehicle object
    """
    vehicle = storage.get(Vehicle, vehicle_id)
    if not vehicle:
        abort(404)

    return jsonify(vehicle.to_dict())


@create_app.route('/vehicless/<vehicle_id>', methods=['DELETE'],
                strict_slashes=False)
@swag_from('documentation/vehicles/delete_vehicles.yml', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    """
    Deletes a Vehicle Object
    """

    vehicle = storage.get(Vehicle, vehicle_id)

    if not vehicle:
        abort(404)

    storage.delete(vehicle)
    storage.save()

    return make_response(jsonify({}), 200)


@create_app.route('/carriers/<carrier_id>/reviews', methods=['POST'],
                strict_slashes=False)
@swag_from('documentation/vehicles/post_vehicles.yml', methods=['POST'])
def post_vehicle(carrier_id):
    """
    Creates a vehicle
    """
    carrier = storage.get(Carrier, carrier_id)

    if not carrier:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'vehicle_type' not in request.get_json():
        abort(400, description="Missing vehicle_type")

    if 'cargo_capacity' not in request.get_json():
        abort(400, description="Missing cargo_capacity")

    if 'plate_number' not in request.get_json():
        abort(400, description="Missing plate_number")

    if 'color' not in request.get_json():
        abort(400, description="Missing color")        

    data = request.get_json()
    data['carrier_id'] = carrier_id
    instance = Vehicle(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@create_app.route('/vehicles/<vehicle_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/vehicles/put_vehicle.yml', methods=['PUT'])
def put_vehicle(vehicle_id):
    """
    Updates a vehicle object
    """
    vehicle = storage.get(Vehicle, vehicle_id)

    if not vehicle:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'carrier_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(vehicle, key, value)
    storage.save()
    return make_response(jsonify(vehicle.to_dict()), 200)