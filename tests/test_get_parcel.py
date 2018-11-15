from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):

    def test_get_empty_parcel_delivery_order_list(self):
        get_request = self.test_client.get("/api/v1/parcels")
        response = json.loads(get_request.data.decode())
        self.assertEqual(response["message"], "No parcels available at the moment")
        self.assertEqual(get_request.status_code, 200)







# class Endpoints(Base):

#     # def test_get_empty_parcel_delivery_order_list(self):
#     #     get_request = self.app_client.get("/api/v1/parcels")
#     #     response = json.loads(get_request.data.decode())
#     #     self.assertIn(test_parcel, response['Parcels'])
#     #     self.assertEqual(get_request.status_code, 200)
#     def test_get_parcel_delivery_order_(self):
#         parcel = {
#             'email': 'kalug@mail.com',
#             'user_id':'1',
#             'status':'pending'

#             }
            

#         get_request = self.app_client.get("/api/v1/parcels", content_type='application/json', data=json.dumps(parcel))
#         response = json.loads(get_request.data.decode())
#         self.assertIn("No parcels available at the moment", response['message'])
#         self.assertEqual(get_request.status_code, 200)

#     def test_get_parcel_delivery_order_with_available_orders(self):
#         parcel = {
#         'order_id' : 1,
#         'user_id' :1,
#         'email':'email@yahdj.com',
#         'status':'pending'

#             }
            

#         # get_request = self.app_client.get("/api/v1/parcels")
#         # self.assertEqual(get_request.status_code, 404)

#     def test_get_all_parcel_delivery_orders_by_specific_user(self):
#         get_request = self.app_client.get("/api/v1/users/1/parcels")
#         self.assertEqual(get_request.status_code, 200)

#     # def test_get_all_parcel_delivery_orders_by_non_user(self):
#     #     get_request = self.app_client.get("/api/v1/users/2/parcels")
#     #     response = json.loads(get_request.data.decode())
#     #     self.assertEqual(response["message"], "There are no parcels delivery orders created by that user or the user does not exist")
#     #     self.assertEqual(get_request.status_code, 200)

#     # def test_get_parcel(self):
#     #     get_request = self.app_client.get("/api/v1/parcels/1")
#     #     self.assertEqual(get_request.status_code, 200)

#     # def test_get_non_existent_parcel(self):
#     #     get_request = self.app_client.get("/api/v1/parcels/400")
#     #     response = json.loads(get_request.data.decode())
#     #     self.assertEqual(response['message'], "Parcel with ID 400 does not exist")
#     #     self.assertEqual(get_request.status_code, 200)

# if __name__ == ('__main__'):
#     unittest.main()