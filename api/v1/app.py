#!/usr/bin/python3
""" Sets up the flask application with configurations """
from api.v1.views import app_views
from flask import Flask
from models import storage
import os

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(ctx):
    """ Closes the current storage connection """
    storage.close()


if __name__ == "__main__":
    API_HOST = os.getenv("HBNB_API_HOST", "0.0.0.0")
    API_PORT = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=API_HOST, port=API_PORT, threaded=True)
