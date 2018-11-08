from flask import Flask, request, abort, jsonify
from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, request
import jwt
from api.models import Models
from api.users import User

app = Flask(__name__)
api = Api(app)


        return 'welcome to getIt Application. For all you Deliveries'

users = [User("Kataala", "Kats",
                   "llkldf@gmail.com", "Debra", "boosiko", True)]
models = Models(users)

class Welcome(Resource):
    def get(self):
        return "WELCOME TO SENDIT APPLICATION"

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

api.add_resource(Welcome, '/')
api.add_resource(Welcome, '/api/v1/register')