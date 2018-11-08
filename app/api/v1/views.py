from flask_restful import Resource
from .models import Parcel

product = Parcel('sender', 'recipient', 'destination', 'weight', 'pickup')


class GenericParcel(Resource, Parcel):
    """This class contains generic parcels without
    any specificity."""

    # def __init__(self, sender, recipient, destination, weight, pickup):
    #     self.product = Parcel()

    def get(self):
        parcel = self.product.get_all()
        return parcel


class SpecificParcel(Resource, Parcel):
    """This class contains methods for manipulating a specific parcel"""

    # def __init__(self, sender, recipient, destination, weight, pickup):
    #     self.product = Parcel()

    def get(self, id):
        """This method should return a parcel if we are sent it's id"""
        parcel = self.product.get_parcel(id)
        return parcel
        # else:
        #     return {"message" : "Parcel does not exist"}, 404

    def post(self):
        """This method is for adding a delivery to our database."""
        add = self.product.add_parcel()
        return add

    def put(self, id):
        """This method should be used to change the destination
        of a del"""
        new = self.product.change_location(id)
        return new
        # for parcel in parcels:
        #     if parcel['id'] == id:
        #         #change the destination
        #         pass
        #     else:
        #         return{"message" : "No such delivery was found"}, 400

    def delete(self, id):
        """This method is for deleting a specific delivery from our
        database"""
        self.product.delete_parcel(id)
        return {"Success": "Delivery {} was successfully deleted".format(id)}


class User(Resource, Parcel):
    """This class represents the user and what actions they can do to their
    parcels"""

    # def __init__(self, sender, recipient, destination, weight, pickup):
    #     self.product = Parcel()

    def get(self, sender):
        """This method gets all deliveries sent by a user"""
        p = self.product.get_theirs(sender)
        if p['sender'] == sender:
            return {"parcels": p}
        else:
            return "No delivery by {}".format(sender)
