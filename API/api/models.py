from werkzeug.security import safe_str_cmp
import jwt
import datetime
from flask import jsonify
from flask import request


class Models:

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


    def search_list(self, username):
        """function to search a list of users for a specific username"""
        for item in self.users:
            if item.get_username() == username:
                return item
            else:
                return None

