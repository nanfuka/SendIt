from flask import Flask, request, abort, jsonify
from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, request
import jwt
from api.models import Models
from api.users import User
from api.orders import Orders
from api.responses import *
app = Flask(__name__)
api = Api(app)
        

users = [User("Kataala", "Kats",
                   "llkldf@gmail.com", "Deb", "kwick")]

orders = [Orders( 'kal@gmail', 'mahogany', 21, 'Nairobi', 'Deb', 'Uganda-Mattuga', 123),  Orders(
    'bal@gmail', 'chaff', 100, 'Rwanda', 'Deb', 'Malawi', 123)]
models = Models(users, orders)

class Welcome(Resource):
    def get(self):
        return 'welcome to getIt Application. For all you Deliveries'

class register_user(Resource):
    def post(self):
        """signup a new user"""
        data = request.args
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        if first_name is not None and last_name is not None and \
            email is not None and username is not None and \
            password is not None:
            user = models.search_list(username)
            if user is None:
                response = models.create_user(
                    User(
                        first_name, last_name, email, username, password)).\
                    get_dictionary()

            else:
                return jsonify("login_fail, fill in all the fields"), 401
        else:
            return jsonify("create_request_fail")

class login(Resource):
    def post(self):
        """login"""

        data = request.get_json(force=True)
        username = data.get('username', None)
        password = data.get('password', None)

        user = models.search_list(username)
        if user is not None:
            if user.verify_password(password):
                response = user.get_dictionary()
           
                return jsonify("response")
            else:
                return jsonify("login_fail"), 200
        else:
            return jsonify("login_fail"), 200

class Place_Orders(Resource):
    def post(self, current_user):


        """api end point for placing a mail delivery order"""
        data = request.get_json(force=True)

    
        email = data.get('email', None)
        item_to_be_shipped = data.get('item_to_be_shipped', None)
        weight = data.get('weight', None)
        itemcurrentlocation = data.get('itemcurrentlocation', None)
        destination = data.get('destination', None)

        if email is not None and item_to_be_shipped \
            is not None and weight is not None and itemcurrentlocation is not None and destination is not None:
            requests = Orders(email, item_to_be_shipped, weight, destination,  current_user.get_username(), itemcurrentlocation)
            create_request_successful['data'] = models.add_orders(
            requests).get_dictionary()
            return jsonify(create_request_successful)
        else:
            return jsonify(create_request_fail)



api.add_resource(Welcome, '/')
api.add_resource(register_user, '/api/v1/register')
api.add_resource (login, '/api/v1/login')
api.add_resource (Place_Orders, '/api/v1/orders')
