import unittest
import os
import json

from run import app
from app.api.v1.views import GenericParcel, SpecificParcel, User


class SpecicicParcelTestCase(unittest.TestCase):

    def setUp(self):
        """This should be called before each test"""
        self.client = app.test_client

        self.parcel = {
            'id': '1',
            'sender': 'Mandela'
            'recipient': 'Jane',
            'destination': 'Heaven',
            'weight': '69',
            'pickup': 'Hell'
        }

    def test
