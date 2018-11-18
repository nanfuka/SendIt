# from api.views import app
# from database_conn import Database
# import unittest
# import json
# # from tests.getToken import GetToken


# class BaseTest(unittest.TestCase):
#     def setUp(self):
#         """Initialisez app and defines variables"""
#         app.testing = True
#         self.test_client = app.test_client()
#         self.database = Database()
#         self.database.create_table_parsels()
#         self.database.create_table_users()
      
#         self.user = {
#             'username': 'joshua', 'email': 'joshua@gmail.com',
#             'password': 'yes'
#             }

#     def tearDown(self):
#         """Crashes down all initialized variables"""
#         self.database.cursor.execute("DROP TABLE parcels")
#         self.database.cursor.execute("DROP TABLE users")
#         self.test_client = None

    # def test_create_user(self):
    #     """create a new user"""
    #     response = self.test_client.post('/api/v1/register', data=self.user)
    #     self.assertEqual(201, response.status_code)
    #     self.assertIn('User created successfully', str(response.data))

    # def test_login_user(self):
    #     """tests api for user login"""
    #     response = self.tester.post('/api/v1/auth/signup', data=self.user)
    #     self.assertEqual(201, response.status_code)
    #     self.assertIn('User created successfully', str(response.data))
    #     response = self.tester.post('/api/v1/auth/login', data=self.user)
    #     self.assertEqual(200, response.status_code)
    #     self.assertIn('You are successfully logged in', str(response.data))

    # def test_admin_signin(self):
    #     """tests api for admin login"""
    #     response = self.tester.post('/api/v1/auth/login', data={
    #         'username': 'admin',
    #         'password': 'mynameisadmin'})
    #     self.assertEqual(200, response.status_code)
    #     self.assertIn('welcome admin', str(response.data))
        

# import unittest
# from api.views import app
# import json
# from database_conn import Database

# db = Database()
# class BaseTestCase(unittest.TestCase):

#     def setUp(self):

#         app.testing = True
#         self.test_client = app.test_client()
#         self.database = Database()
#         self.database.create_table_parsels()
#         self.database.create_table_users()

#         self.user = {
#             'username': 'precious',
#             'email': 'mwendi@gmail.com',
#             'password': 'matengu@gmail.com'
#         }

#         self.user_login_data={
#             "username":"grace",
#             "password":"myprecious"
#         }  
#     def tearDown(self):
#         pass
# if __name__ == "__main__":
#     unittest.main()