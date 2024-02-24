#!/usr/bin/python3
""" """
import unittest
from api.v1.app import app


class TestStatus(unittest.TestCase):
    """ """
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        """ """
        self.ctx.pop()

    def test_status_if_ok(self):
        """ """
        with app.test_client() as client:
            response = client.get("/api/v1/status")
            data = response.get_json()
            self.assertDictEqual(
                    data,
                    {"status": "OK"}
                    )
