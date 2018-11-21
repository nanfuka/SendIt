from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):
    def test_get_all_parcel_delivery_orders_by_specific_user(self):
        get_request = self.test_client.get("/api/v1/users/1/parcels")
        self.assertEqual(get_request.status_code, 400)
