from flask import Flask
from flask_restful import Api, Resource
from .models import Parcel


class GenericParcel(Resource, Parcel):
    """This class contains generic parcel data > data without any
    specificity."""
    def __init__(self):
        pass

    def get(self, id):
        parcels = Parcel.get_all
        return parcels


    def delete(self, id):
        pass

    def put(self, id):
        pass

    def post(self, id):
        pass

class SpecificParcel(Resource):
    """This class contains methods for manipulating a specific parcel"""
    def get(self):
        pass
