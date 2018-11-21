from app import app
import unittest
import json


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()

        self.order = {
            "destination": "europ",
            "email": "fd@yaho.com",
            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1
        }
        parcel = {
            "destination": "europ",
            "email": "fd@yaho.com",
            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1
        }

        # self.user_login_data={
        #     "username":"grace",
        #     "password":"myprecious"
        # }
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
