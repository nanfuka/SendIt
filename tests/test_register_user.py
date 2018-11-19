# import unittest
# from api.views import app
# import json
# from database_conn import Database

# db = Database()


# class TestUsers(unittest.TestCase):
#     def setUp(self):
#         """Initialisez app and defines variables"""
#         app.testing = True
#         self.test_client = app.test_client()
#         self.database = Database()
#         # self.database.create_table_parsels()
#         self.database.create_table_users()
      
#         self.user = {
#             'username': 'hotmama', 'email': 'slayqueen@gmail.com',
#             'password': 'jjkdshksjfsjdfhdskjfhsdkj'
#             }
#         self.login_user = {'username':'hotmama', 'password':'jjkdshksjfsjdfhdskjfhsdkj'}
    
#     def tearDown(self):
#         """Crashes down all initialized variables"""
#         # self.database.cursor.execute("DROP TABLE parcels")
#         self.database.cursor.execute("DROP TABLE users")
#         self.test_client = None
# #         self.test_client = app.test_client(self)

#     def test_user_register(self):

#         response = self.test_client.post(
#             'api/v1/register',
#             content_type='application/json',
#             data=json.dumps(self.user)
#         )
#         message = json.loads(response.data.decode())

#         self.assertEqual(message['message'],
#                          'user successfully added')

#     def test_login_user(self):
#         """tests api for user login"""
#         response = self.test_client.post('/api/v1/login', data=self.login_user)
#         self.assertEqual(200, response.status_code)
#         self.assertIn('You are successfully logged in', str(response.data))



# from api.views import app
# from database_conn import Database
# import unittest
# import json
# from tests.tokens import GetToken
# # from api.model.data import Userdata
# from app import app


# class AppTestCase(unittest.TestCase):
#     def setUp(self):
#         """Initialisez app and defines variables"""
#         app.testing = True
#         self.test_client = app.test_client()
#         self.database = Database()
#         self.database.create_table_parsels()
#         self.database.create_table_users()

#         self.user = {
#             'username': 'dora', "email": "dorah@gmail.com", "password":"sddsfgfdg"
            
#             }

#     def tearDown(self):
#         """Crashes down all initialized variables"""
#         self.database.cursor.execute("DROP TABLE parcels")
#         self.database.cursor.execute("DROP TABLE users")
#         self.test_client = None

#     def test_create_user(self):
#         """create a new user"""
#         response = self.test_client.post('/api/v1/register', data=self.user)
#         self.assertEqual(201, response.status_code)
#         self.assertIn('user successfully added', str(response.data))



#     def test_admin_signin(self):b nerbj
#         """tests api for admin login"""
#         response = self.tester.post('/api/v1/login', data={
#             'username': 'admin',
#             'password': 'mynameisadmin'})
#         self.assertEqual(200, response.status_code)
#         self.assertIn('welcome admin', str(response.data))