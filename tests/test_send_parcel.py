from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):

    def test_send_parcel(self):
        """ Tests whether a user can create a request successfully """
        response = self.test_client.post(
            '/api/v1/parcels', data=json.dumps(self.order), content_type='application/json')
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
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your user_id please", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_without_email(self):
        parcel = {
            "destination": "europ",

            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1
        }

        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your email please", response['message'])
        self.assertEqual(post_request.status_code, 400)

    # def test_create_parcel_without_user_id(self):
    #     parcel = {
    #         'user_id':2,
    #         'status':'pending'
    #         }

        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your email please", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_invalid_email(self):
        parcel = {
            "destination": "ecbvurop",
            "email": "fdyacvcho.com",
            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1

        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Invalid email", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_invalid_destination(self):
        parcel = {
            "destination": 1,
            "email": "fdy@cvcho.com",
            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1

        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("The input should be a string", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_empty_item_origin(self):
        parcel = {
            "destination": 1,
            "email": "fdy@cvcho.com",
            "item_origin": " ",
            "item_to_be_shipped": "muucdhx",
            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1

        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("The input should be a string", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_status_with_empty_space_as_input(self):
        parcel = {
            'email': 'kalug@mail.com',
            'user_id': 2,
            'status': ' '

        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your item_to_be_shipped please",
                      response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_user_id_a_string(self):
        parcel = {
            'email': 'kalug@mail.com',
            'user_id': 'joe',

            'status': 'pending'

        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("The input should be a number", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_empty_item_item_to_be_shiped(self):
        parcel = {
            "destination": 1,
            "email": "fdy@cvcho.com",
            "item_origin": " ",

            "name_of_reciever": "Dorah",
            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1

        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your item_to_be_shipped please",
                      response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_empty_name_of_reciever(self):
        parcel = {
            "destination": "europ",
            "email": "fd@yaho.com",
            "item_origin": "nsambya",
            "item_to_be_shipped": "muucdhx",

            "order_id": 1,
            "status": "pending",
            "user_id": 1,
            "weight": 1

        }
        post_request = self.test_client.post(
            "/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your name_of_reciever please",
                      response['message'])
        self.assertEqual(post_request.status_code, 400)
