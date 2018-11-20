from api.views import app
from database_conn import Database
import unittest
import json
from tests.tokens import GetToken


class AppTestCase(unittest.TestCase):
    def setUp(self):
        """Initialisez app and defines variables"""
        self.tester = app.test_client()
        self.database = Database()
        self.database.create_table_users()
        self.database.create_table_parsels()

  
        self.user = {
            'username': 'debbbs', 'email': 'deb@gmail.com',
            'password': 'debeatsfood'
            }
        self.admin{
            'username':'admin', 'password':'admin'
        }

    def tearDown(self):
        """Crashes down all initialized variables"""
        self.database.cursor.execute("DROP TABLE parcels")
        self.database.cursor.execute("DROP TABLE users")


    def test_create_user(self):
        """create a new user"""
        response = self.tester.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
        self.assertEqual(201, response.status_code)
        self.assertIn ("user successfully added", str(response.data))

    def test_login_user(self):
        """tests api for user login"""
        response = self.tester.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
        self.assertEqual(201, response.status_code)
        self.assertIn('user successfully added', str(response.data))
        response = self.tester.post('/api/v1/auth/login', data=json.dumps(self.user), content_type ='application/json')
        self.assertEqual(200, response.status_code)
        self.assertIn('You are successfully logged in', str(response.data))

    def test_admin_signin(self):
        """tests api for admin login"""
        response = self.tester.post('/api/v1/auth/signup', data=json.dumps(self.admin), content_type ='application/json')
        self.assertEqual(201, response.status_code)
        self.assertIn('user successfully added', str(response.data))
        response = self.tester.post('/api/v1/auth/login', data=json.dumps(self.admin), content_type ='application/json')
        self.assertEqual(200, response.status_code)
        self.assertIn('You are successfully logged in', str(response.data))
        
