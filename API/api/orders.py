import uuid
class Orders:

    def __init__(
            self, email, item_to_be_shipped, weight, destination, username, itemcurrentlocation, order_Id=str(
                uuid.uuid4())):
        self.order_Id = order_Id
        self.email = email
        self.item_to_be_shipped = item_to_be_shipped
        self.weight = weight
        self.owner = username
        self.destination = destination
        self.itemcurrentlocation = itemcurrentlocation

    def get_dictionary(self):
        return {
            'email': self.email,
            'item_to_be_shipped': self.item_to_be_shipped,
            'weight': self.weight,
            'owner': self.owner,
            'destination': self.destination,
            'itemcurrentlocation': self.itemcurrentlocation,
            'order_Id': self.order_Id
        }

    def get_owner(self):
        return self.owner

    def get_order_Id(self):
        return self.order_Id