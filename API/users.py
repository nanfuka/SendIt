import json
from flask import jsonify

ids = []
users =[]
class User:
    def __init__(self, user_Id, first_name, last_name, email,
                username, password):
        self.user_Id = len(ids)+1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = self.password
        
        

    def get_dictionary(self):
        return{
            'user_Id': self.user_Id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username,
            'password':self.password
        }