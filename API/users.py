class User:

    def __init__(self,user_name,user_id, email):
        self.username = user_name
        self.user_id = user_id


class Parcel:
    #def __init__(self, order_id, user_id, email, item_to_be_shipped, weight, name_of_sender, name_of_reciever, destination, username, itemcurrentlocation):
    def __init__(self, order_id,status):    
        self.order_Id = order_id

        # self.item_to_be_shipped = item_to_be_shipped
        # self.weight = weight
        # self.name_of_sender = name_of_sender
        # self.name_of_reciever = name_of_reciever
        # self.destination = destination
        # self.username = username
        # self.itemcurrentlocation = itemcurrentlocation

