from flask import request

# this is where all our parcels will be appended
parcels = []


class Parcel(object):
    """This is the parcel class"""

    def __init__(self, sender, recipient, destination, weight, pickup):
        self.db = parcels
        self.sender = sender
        self.recipient = recipient
        self.destination = destination
        self.weight = weight
        self.pickup = pickup

    def add_parcel(self):
        """The method to create a delivery and append
            it to our list"""

        # we check the request object the user sends to
        # validate it has enough information
        if not request.json():
            return {"Error": "Bad request"}, 400
        if not request.json['sender']:
            return {"Error": "Please include the sender name"}, 400
        if not request.json["recipient"]:
            return {"Error": "Please include the recipient"}, 400
        if not request.json["destination"]:
            return {"Error": "You must specify a destination"}, 400
        if not request.json["weight"]:
            return {"Error": "You must specify the weight"}, 400
        if not request.json["pickup"]:
            return {"Error": "What is the pickup location?"}, 400

        data = {
            'id': len(parcels) + 1,
            'sender': request.json['sender'],
            'recipient': request.json['recipient'],
            'destination': request.json['destination'],
            'weight': request.json['weight'],
            'pickup': request.json['pickup']
        }

        self.db.append(data)
        return {"Success": "Added parcel" + data}, 201

    def get_all(self):
        """Defines the method to get all parcel deliveries GET /parcels"""
        return {"parcels": self.db}, 200

    def get_parcel(self, id):
        """Defines method to get a specific delivery with it's key
         GET /parcels/<int:id>"""
        for p in self.db:
            if p['id'] == id:
                return p, 200
            else:
                return {"Error": "No delivery exists with that id."}, 404

    def delete_parcel(self, id):
        """Defines the method for deleting a specific delivery from the
        database"""
        for p in self.db:
            if len(p) == 0:
                return {"message": "Delivery not found."}, 400
            elif p['id'] == id:
                self.db.remove(p)
                return {"Success": "Delivery successfully deleted."}, 200
            else:
                return {"Error": "No delivery exists with that id."}, 404

    def get_theirs(self, sender):
        """"Defines the method for getting all deliveries from a specific
        sender"""
        if not request.json("sender"):
            return {"Error": "Please include your sender"}
        for p in parcels:
            if p["sender"] == sender:
                return {"Parcels by {}".format(sender), p}, 200
        else:
            return "No delivery by {}".format(sender), 404

    def change_location(self, id):
        """Defines the method for changing the
        current location of a delivery"""
        for p in parcels:
            if p["id"] == id:
                if not request.json["location"]:
                    return {"Error": "You must add a location"}, 400
                else:
                    location = request.json["location"]
                    p["location"] = location
                    return p, 201
            else:
                return "Parcel not found", 404

    def change_destination(self, id):
        if not request.json["destination"]:
            return {"Error": "Please enter your new destination"}, 400
        new = request.json["destination"]
        for p in parcels:
            if p["id"] == id:
                p["destination"] = new
                return {"Success": "Destination successfully changed" + p}, 200
