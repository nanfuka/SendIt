# from API.views import app
from API.views import app
import unittest
import json

class AppTestCase(unittest.TestCase):
    def setUp(self):
        """Initialises app and sets its variables"""
        app.testing = True
        self.tester = app.test_client()
        self.order = {'user_id':'deb', 'email':'kalungi2k4@ds.com','status':'pending'
            }
    
    def tearDown(self):
        """Crashes down all initialized variables"""
        self.tester = None

    def test_index(self):
        response = self.tester.get('/')
        self.assertTrue(200, response.status_code)
        self.assertIn('WELCOME TO SEND_IT APP, THE SOLUTION TO ALL YOUR COUREER SERVICES', str(response.data))
    

if __name__ == ('__main__'):
    unittest.main()