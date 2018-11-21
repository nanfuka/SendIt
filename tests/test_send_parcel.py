from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):
    def test_send_parcel(self):
        """ Tests whether a user can create a request successfully """
        parcel = {
            "username":"deb",
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
        response = self.test_client.post(
            '/api/v1/parcels', data=json.dumps(parcel),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue("parcel successfully created")

    def test_create_parcel_without_user_id(self):
        parcel = {
            "destination": "europ",
            "email": "fd@yaho.com",
            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",

            "weight": 1
        }
        post_request = self.test_client.post(
            "/api/v1/parcels",
            content_type='application/json',
            data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your user_id please", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_without_destination(self):
        parcel = {

            "email": "fd@yaho.com",
            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1
        }
        post_request = self.test_client.post(
            "/api/v1/parcels",
            content_type='application/json',
            data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your destination please", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_without_email(self):
        parcel = {
            "destination": "vcxvc",

            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1
        }
        post_request = self.test_client.post(
            "/api/v1/parcels",
            content_type='application/json',
            data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your email please",
                      response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_without_item_origin(self):
        parcel = {
            "destination": "vcxvc",
            "email": "hsdhdsh@gmail.com",

            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1
        }
        post_request = self.test_client.post(
            "/api/v1/parcels",
            content_type='application/json',
            data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your item_origin please", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_without_item_item_to_be_shipped(self):
        parcel = {
            "destination": "vcxvc",
            "email": "hsdhdsh@gmail.com",

            "item_origin": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1
        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json',
            data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your item_to_be_shipped please",
                      response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_without_name_of_reciever(self):
        parcel = {
            "destination": "vcxvc",
            "email": "hsdhdsh@gmail.com",

            "item_origin": "muucdhx",
            "item_to_be_shipped": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1
        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json',
            data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your name_of_reciever please",
                      response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_without_weight(self):
        parcel = {
            "destination": "vcxvc",
            "email": "hsdhdsh@gmail.com",

            "item_origin": "muucdhx",
            "item_to_be_shipped": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "name_of_reciever": "maggie"
        }
        post_request = self.test_client.post(
            "/api/v1/parcels",
            content_type='application/json',
            data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your weight please", response['message'])
        self.assertEqual(post_request.status_code, 400)
