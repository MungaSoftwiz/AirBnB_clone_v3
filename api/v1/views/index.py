#!/usr/bin/python3
""" Creates a route """
from flask import jsonify, request
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=['GET'])
def status():
    """ Creates a route that returns JSON """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=['GET'])
def stats():
    """Retrieves the number of each objects by type"""
    if request.method == "GET":
        reps = {}
        objs = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for k, v in objs.items():
            reps[v] = storage.count(k)
        return jsonify(reps)
