# from werkzeug.security import safe_str_cmp
# import jwt


# from functools import wraps
from flask import request, jsonify
from database_conn import Database
import re

class Userdata:
    def __init__(self):
        self.database = Database()
        self.database.create_table_users()
        self.database.create_table_parsels()

    def create_user(self):
        user_data = request.get_json()
        username = user_data.get('username')
        email = user_data.get('email')
        password = user_data.get('password')

        if not user_data:
            return jsonify({'message': 'All fields are required'}), 400
        if not username or username == " " or username == type(int):
                return jsonify({'message': 'Invalid username'}), 400

        if not email or not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email) or email ==" ":
            return jsonify({
                "status": "Fail",
                "message": "Enter valid email"}), 400
                    
        if not password or password == " " or len(password) < 5:
            return jsonify({'message': 'A stronger password  is required'}), 400
    
        if self.find_user_by_username(user_data['username']):
            return jsonify({'message': 'username already exists, please choose another username'}), 409

        elif user_data['username'].isspace():
            return {'message': 'Field cannot be blank'}, 400    
        
        specialCharacters = ['$','#','@','!','*']

        if any(char in specialCharacters for char in (user_data['username'])):
            return {'message': 'username cannot have special characters'}, 400

        elif self.find_user_by_email(user_data['email']):
            return jsonify({'message': 'please use another email address, that one is taken'}), 400


        else:
            query = ("INSERT INTO users(username, email, password)\
                VALUES('{}', '{}', '{}')\
                RETURNING user_id, username, email, password")

            self.database.cursor.execute(query.format(user_data['username'],
                user_data['email'], user_data['password']))

            return jsonify({"message": "user successfully added", "user":user_data['username']}), 201
    
    def find_user_by_username(self, username):
        query = "SELECT * FROM  users WHERE username = '{}'"
        self.database.cursor.execute(query.format(username))
        row = self.database.cursor.fetchone()
        return row

    def find_user_by_email(self, email):
        query = "SELECT * FROM  users WHERE email = '{}'"
        self.database.cursor.execute(query.format(email))
        row = self.database.cursor.fetchone()
        return row
