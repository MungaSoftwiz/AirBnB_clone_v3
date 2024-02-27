#!/usr/bin/python3
""" Contains city APIs """
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
import json


@app_views.route(
        "/states/<state_id>/cities",
        methods=["GET", "POST"],
        strict_slashes=False
        )
def list_cities(state_id):
    """ Lists cities of a given state id """
    state_obj = storage.get(State, state_id)
    if request.method == "GET":
        if not state_obj:
            abort(404)
        cities_list = [city.to_dict() for city in state_obj.cities]
        return jsonify(cities_list)
    if request.method == "POST":
        if not state_obj:
            abort(404)
        if not request.is_json:
            abort(400, description="Not a JSON")
        json_data = request.get_json()
        if "name" not in json_data:
            abort(400, description="Missing name")
        json_data["state_id"] = state_id
        new_city_obj = City(**json_data)
        storage.new(new_city_obj)
        storage.save()
        return make_response(jsonify(new_city_obj.to_dict()), 201)


@app_views.route(
        "/cities/<city_id>",
        methods=["GET", "DELETE", "PUT"],
        strict_slashes=False
        )
def retrieve_cities_object(city_id):
    """ Returns city object representation """
    city_obj = storage.get(City, city_id)
    if request.method == "GET":
        if not city_obj:
            abort(404)
        city_repr = city_obj.to_dict()
        return jsonify(city_repr)
    if request.method == "DELETE":
        if not city_obj:
            abort(404)
        storage.delete(city_obj)
        storage.save()
        return make_response(jsonify({}), 200)
    if request.method == "PUT":
        if not city_obj:
            abort(404)
        if not request.is_json:
            abort(400, description="Not a JSON")
        user_data = request.get_json()
        ignored_keys = ["id", "state_id", "created_at", "updated_at"]
        for key in user_data:
            if key not in ignored_keys:
                setattr(city_obj, key, user_data[key])
        storage.save()
        return make_response(jsonify(city_obj.to_dict()), 200)
