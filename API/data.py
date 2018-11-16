from werkzeug.security import safe_str_cmp
import jwt
import datetime
from flask import jsonify

from functools import wraps
from flask import request


class DataStore:

    def __init__(self, users=[]):

        self.users = users

       
        self.key = "my Jesus I love thee"

    def create_user(self, user):
        """
        function to create a new user and append
        new user to the list of users
        """
        self.users.append(user)
        return user

    # def update_order(self, order):
    #     """function to update an order"""
    #     i = 0
    #     for req in self.orders:
    #         if req.get_order_Id() == order.get_order_Id():
    #             self.orders[i] = order
    #             return order.get_dictionary()
    #         i = i+1
    #     return None

    def search_list(self, username):
        """function to search a list of users for a specific username"""
        for item in self.users:
            if item.get_username() == username:
                return item
            else:
                return None

    def generate_auth_token(self, user):
        """function to generate an auth-token"""
        try:
            payload = {
                'exp': datetime.datetime.utcnow(

                ) + datetime.timedelta(minutes=2000),
                'iat': datetime.datetime.utcnow(),
                'user': user
            }
            return jwt.encode(
                payload,
                self.key,
                algorithm='HS256'
            ).decode('utf-8')
        except Exception as e:
            return e

    def token_required(self, func):

        @wraps(func)
        def decorated(*args, **kwargs):
            token = None
            if "Authorization" in request.headers:
                token = request.headers['Authorization']
            else:
                return jsonify({"message":"auth_fail"}), 401
            try:
                data = jwt.decode(token, self.key)
                current_user = self.search_list(data['user']['username'])
            except:
                return jsonify({"message":"auth_fail"}), 401
            return func(current_user, *args, **kwargs)
        return decorated
