from app import app
import unittest
import json
class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()
        # self.user_data = {
        #     "user_id": 1,
        #     "name": "debbie",
        #     "email":"kalungi2k6@gmail.com",
        #     "username":"grace",
        #     "password":"myprecious"
           
        # }
        # self.menu = {
        #     "menu_id": 1,
        #     "menu_name": "chips",
        #     "price":200           
        # }
        self.order = {
            "email": "kk@email.com ", 
            "order_id": 1, 
            "status": "pen", 
            "user_id": 4         
        }

        # self.user_login_data={
        #     "username":"grace",
        #     "password":"myprecious"
        # }  
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()