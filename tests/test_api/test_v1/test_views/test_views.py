#!/usr/bin/python3
""" Tests json responses for the APIs"""
import unittest
from api.v1.app import app


class TestStatus(unittest.TestCase):
    """ Tests status behavious of the api """
    def setUp(self):
        """ Sets up an application context """
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        """ Tears down an application context """
        self.ctx.pop()

    def test_status_if_ok(self):
        """ Test if API returns correct status"""
        with app.test_client() as client:
            response = client.get("/api/v1/status")
            data = response.get_json()
            self.assertDictEqual(
                    data,
                    {"status": "OK"}
                    )
