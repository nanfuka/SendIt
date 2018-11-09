from unittest import TestCase
from flask import json
from API.api.views import app
from API.api.users import User
import unittest


class BaseTest(TestCase):

    def setUp(self):
        """
        initialise the app module
        create a pytest fixture called client() 
        that configures the application for testing
        """
        self.app = app
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        """Release Context"""
        self.context.pop()

    def get_auth_token(self):
        """create token from login"""
        response = self.client.post('/api/v1/login',
                                    content_type='application/json',
                                    data=json.dumps(dict(username='Deb',
                                                         password='boosiko')))
        reply = json.loads(response.data.decode())
        self.assertEquals(reply['success'], True)
        if reply['success']:
            return reply['token']
        else:
            return None

    def get_request_id(self):
        """Get Request Id for Test Purposes"""
        head = {'Authorization': self.get_auth_token(
        ), 'content_type': 'application/json'}

        request = {'email': 'kal@gmail', 'item_to_be_shipped':'mahogany', 'weight':21,
        'destination':'Nairobi','itemcurrentlocation':'Uganda-Mattuga', 'owner':'Deb' }

        response = self.client.post(
            '/api/v1/parcels', headers=head, data=json.dumps(request))
        reply = json.loads(response.data.decode())
        assert "200 OK" == response.status
        if reply['success']:
            return reply['data']['id']