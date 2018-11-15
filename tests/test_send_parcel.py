from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):
    
    def test_send_parcel(self):
        """ Tests whether a user can create a request successfully """
        response = self.test_client.post('/api/v1/parcels', data=json.dumps(self.order), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue("parcel successfully created")

    def test_create_parcel_without_user_id(self):
        parcel = {
            'email':'kalungi2k4@ds.com',
            'status':'pending'
            }
        post_request = self.test_client.post("/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your user_id please", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_without_email(self):
        parcel = {
            'user_id':2,
            'status':'pending'
            }
    
        post_request = self.test_client.post("/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Enter your email please", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_invalid_input(self):
        parcel = {
            'email': 'kalu@gmail.com',
            'user_id':2,
            'status':'pendi#ng'

            }
        post_request = self.test_client.post("/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("status cannot have special characters", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_invalid_email(self):
        parcel = {
            'email': 'kalugmail.com',
            'user_id':2,
            'status':'pendi#ng'

            }
        post_request = self.test_client.post("/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Invalid email", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_status_with_empty_space_as_input(self):
        parcel = {
            'email': 'kalug@mail.com',
            'user_id':2,
            'status':' '

            }
        post_request = self.test_client.post("/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("Field cannot be blank", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_create_parcel_with_user_id_a_string(self):
        parcel = {
            'email': 'kalug@mail.com',
            'user_id':'joe',
        
            'status':'pending'

            }
        post_request = self.test_client.post("/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
        response = json.loads(post_request.data.decode())
        self.assertIn("The user_id should be an integer", response['message'])
        self.assertEqual(post_request.status_code, 200)
        