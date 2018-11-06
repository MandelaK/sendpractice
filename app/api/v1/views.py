from flask import Flask
from flask_restful import Api, Resource
from .models import Parcel

class GenericParcel(Resource, Parcel):
    """This class contains generic parcel data > parcels without any
    specificity."""
    def __init__(self):
        pass

    def get(self:
        parcels = Parcel.get_all()
        return parcels

class SpecificParcel(Resource, Parcel):
    """This class contains methods for manipulating a specific parcel"""
    def get(self, id):
        """This method should return a parcel if we are sent it's id"""
        for parcel in Parcel.parcels:
            if parcel["id"] == id:
                return {"parcel" : parcel}
            else:
                return {"message" : "Parcel does not exist"}, 404

    def post(self):
        """This method is for adding a delivery to our database."""
        #pass

    def put(self, id):
        """This method should be used to change the destination
        of a del"""
        for parcel in Parcel.parcels:
            if parcel['id'] == id:
                #change the destination
                pass
            else:
                return{"message" : "No such delivery was found"}, 400

    def delete(self, id):
        """This method is for deleting a specific delivery from our
        database"""
        for parcel in Parcel.parcels:
            if parcel['id'] == id:
                #delete the parcel
                pass
            else:
                return {"message" : "No such delivery was found"}, 400

class User(Resource, Parcel):
    """This class represents the user and what actions they can do to their
    parcels"""
    def get(self, sender):
        """This method gets all deliveries sent by a user"""
        for parcel in Parcel.parcels:
            if parcel['sender'] == sender:
                return {"parcels" : parcel}
            else:
                return "No delivery by {}".format(sender), 400
