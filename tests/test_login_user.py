import unittest
from api.views import app
import json
from database_conn import Database

db = Database()


class TestUsers(unittest.TestCase):
    def setUp(self):
        """Initialisez app and defines variables"""
        app.testing = True
        self.test_client = app.test_client()
        self.database = Database()
        self.database.create_table_parsels()
        self.database.create_table_users()
      
        self.user = {
            'username': 'hotmama', 'email': 'slayqueen@gmail.com',
            'password': 'jjkdshksjfsjdfhdskjfhsdkj'
            }
        self.login_user = {'username':'hotmama', 'password':'jjkdshksjfsjdfhdskjfhsdkj'}
    
    def tearDown(self):
        """Crashes down all initialized variables"""
        self.database.cursor.execute("DROP TABLE parcels")
        self.database.cursor.execute("DROP TABLE users")
        self.test_client = None
#         self.test_client = app.test_client(self)

    def test_user_register(self):

        response = self.test_client.post(
            'api/v1/register',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'user successfully added')