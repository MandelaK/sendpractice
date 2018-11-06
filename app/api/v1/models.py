parcels = []

class Parcel(object):
    """This is the parcel class"""

    def add_parcel(self, sender, recipient, destination, weight, pickup):
        """The method to create a delivery and append it to our list"""
        self.sender = sender
        self.recipient = recipient
        self.destination = destination
        self.weight = weight
        self.pickup = pickup

        #this is our payload, our gold
        gold = {
        "id" : len(parcels) + 1,
        "sender" : self.sender,
        "recipient" : self.recipient,
        "destination" : self.destination,
        "weight" : self.weight,
        "pickup" : self.pickup
        }

        parcels.append(gold)
        return 201

    def get_all(self):
        """Defines the method to get all parcel deliveries GET /parcels"""
        return parcels

    def get_parcel(self, id):
        """Defines method to get a specific delivery with it's key
         GET /parcels/<int:id>"""
        for p in parcels:
            if p['id'] == id:
              return p, 200
            else:
              return 404

    def delete_parcel(self, id):
        """Defines the method for deleting a specific delivery from the
        database"""
        for p in parcels:
            if p['id'] == id:

                return p, 200
            else:
                return 404

    def get_theirs(self, sender):
        """"Defines the method for getting all deliveries from a specific
        sender"""
        for p in parcels:
            if p["sender"] == sender:
                return p, 200
        else:
            return "No delivery by {}".format(sender), 404

    def change_location(self, id, location):
        """Defines the method for changing the current location of a delivery"""
        for p in parcels:
            if p["id"] == id:
                p["location"] = location
                return parcel, 201
            else:
                return "Parcel not found", 404
