from api.views import app
import json
from app import app


class GetToken:

    @staticmethod
    def get_user_token():
        user = {
            'username': 'joshua', 'email': 'joshua@gmail.com',
            'password': 'yes'
            }
        response = app.test_client().post('/api/v1/register', data=user)
        response = app.test_client().post('/api/v1/login', data=user)
        token = json.loads(response.data)['token']
        return token

    @staticmethod
    def get_admin_token():
        user = {
            'username': 'admin',
            'password': 'mynameisadmin'
            }
        response = app.test_client().post('/api/v1/login', data=user)
        token = json.loads(response.data)['token']
        return token
