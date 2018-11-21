from api.views import app
from app import app
from database_conn import Database
import unittest
import json



class AppTestCase(unittest.TestCase):
    def setUp(self):
        """Initialisez app and defines variables"""
        self.test_client = app.test_client()
        self.database = Database()
        self.database.create_table_users()
        self.database.create_table_parsels()

  
        self.user = {
            'username': 'debbbs', 'email': 'deb@gmail.com',
            'password': 'debeatsfood'
            }
        self.admin = {
            'username':'admin', 'password':'admin'
            }

    def tearDown(self):
        """Crashes down all initialized variables"""
        self.database.cursor.execute("DROP TABLE parcels")
        self.database.cursor.execute("DROP TABLE users")


    def test_create_user(self):
        """create a new user"""
        response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
        self.assertEqual(201, response.status_code)
        self.assertIn ("user successfully added", str(response.data))

    