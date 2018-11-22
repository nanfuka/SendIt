# from api.views import app
# from app import app
# from database_conn import Database
# import unittest
# import json



# class AppTestCase(unittest.TestCase):
#     def setUp(self):
#         """Initialisez app and defines variables"""
#         self.test_client = app.test_client()
#         self.database = Database()
#         self.database.create_table_users()
#         self.database.create_table_parsels()

  
#         self.user = {
#             'username': 'debbbs', 'email': 'deb@gmail.com',
#             'password': 'debeatsfood'
#             }
#         self.admin = {
#             'username':'admin', 'password':'admin'
#             }

#     def tearDown(self):
#         """Crashes down all initialized variables"""
#         self.database.cursor.execute("DROP TABLE parcels")
#         self.database.cursor.execute("DROP TABLE users")


#     def test_create_user(self):
#         """tests the response data returned upon user signup
#         """
#         response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
#         self.assertEqual(201, response.status_code)
#         self.assertIn ("user successfully added", str(response.data))

#     def test_create_user_without_inputs(self):
#         """tests whther a user can login without 
#             any input data
#         """
#         self.user = {}
#         response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
#         self.assertEqual(400, response.status_code)
#         self.assertIn ("All fields are required", str(response.data))

#     def test_create_user_without_email(self):
#         """tests wether a user can register without entering the email"""
#         self.user = {'username': 'debbbs','password': 'debeatsfood'}
#         response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
#         self.assertEqual(400, response.status_code)
#         self.assertIn ("Enter valid email", str(response.data))


#     def test_create_user_with_wrong_email_formart(self):
#         """tests for email format upon registration"""
#         self.user = {
#             'username': 'debbbs', 'email': 'debgmail.com',
#             'password': 'debeatsfood'
#             }
#         self.user = {'username': 'debbbs','password': 'debeatsfood'}
#         response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
#         self.assertEqual(400, response.status_code)
#         self.assertIn ("Enter valid email", str(response.data))

#     def test_create_user_without_username(self):
#         """
#         tests if a user can signup without a username
#         """
#         self.user = {
#              'email': 'deb@gmail.com',
#             'password': 'debeatsfood'
#             }
#         response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
#         self.assertEqual(400, response.status_code)
#         self.assertIn ("Invalid username", str(response.data))

#     # def test_create_user_with_empty_strings(self):
#     #     self.user = {
#     #         'username': ' ', 'email': 'deb@gmail.com',
#     #         'password': 'debeatsfood'
#     #         }
#     #     response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
#     #     self.assertEqual(400, response.status_code)
#     #     self.assertIn ("Invalid username", str(response.data))

#     # def test_create_user_with_special_characters(self):
#     #     self.user = {
#     #         'username': "deb%@@", 'email': 'deb@gmail.com',
#     #         'password': 'debeatsfood'
#     #         }
#     #     response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(self.user), content_type ='application/json')
#     #     self.assertEqual(400, response.status_code)
#     #     self.assertIn ("Invalid username", str(response.data))


    