from werkzeug.security import safe_str_cmp
import jwt
import datetime
from flask import jsonify

from functools import wraps
from flask import request
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

        if user_data:
            print(user_data)
        if not user_data:
            return jsonify({'message': 'All fields are required'}), 400
        if not username or username == " " or username == type(int):
            return jsonify({'message': 'Invalid username'}), 400

        if not email or not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
            return jsonify({
                "status": "Fail",
                "message": "Enter valid email"}), 400
                
        if not password or password == " " or len(password) < 5:
            return jsonify({'message': 'A stronger password  is required'}), 400
 
        if self.find_user_by_username(user_data['username']):
            return jsonify({'message': 'username already exists, please choose another username'}), 409
        
        specialCharacters = ['$','#','@','!','*']

        if any(char in specialCharacters for char in (user_data['username'])):
            return {'message': 'username cannot have special characters'}, 400

        elif self.find_user_by_email(user_data['email']):
            return {'message': 'please use another email address'}, 409
        elif user_data['username'].isspace():
            return {'message': 'Field cannot be blank'}, 400

            

        else:
            query = ("INSERT INTO users(username, email, password)\
            VALUES('{}', '{}', '{}')\
            RETURNING user_id, username, email, password")

        self.database.cursor.execute(query.format(user_data['username'],
            user_data['email'], user_data['password']))

        return jsonify({"message": "user successfully added"}), 200

    def find_user_by_username(self, username):
        query = "SELECT * FROM  users WHERE username = '{}'"
        self.database.cursor.execute(query.format(username))
        row = self.database.cursor.fetchone()
        return row

    def login_user(self):
        """user login [POST]"""
        user_data = request.get_json()
        username = user_data.get('username')
        password = user_data.get('password')

        if not user_data:
            return jsonify({'message': 'All fields are required'}), 400
        if not username or username == " " or username == type(int):
            return jsonify({'message': 'Invalid username'}), 400
                
        if not password or password == " " or len(password) < 5:
            return jsonify({'message': 'A stronger password  is required'}), 400
        
        specialCharacters = ['$','#','@','!','*']

        if any(char in specialCharacters for char in (user_data['username'])):
            return jsonify({'message': 'username cannot have special characters'}), 400
        elif user_data['username'].isspace():
            return jsonify({"message": "Field cannot be blank"}), 400
        
        query = "SELECT * FROM users WHERE username = '{}'"
        self.database.cursor.execute(query.format(username))
        if self.find_user_by_name(user_data['username']) and self.find_user_by_password(user_data['password']):
            token = jwt.encode({
                'username': user_data['username'],
                'exp':
                datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                }, 'customerkey')
            response = {'message': 'You are successfully logged in',
                    'token': token.decode('utf-8'), 'user':user_data}, 200
            return jsonify({"message":response})
        
        elif user_data['username'] == 'admin' and user_data['password'] == 'admin':
            token = jwt.encode({
                'username': user_data['username'],
                'exp':
                datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                }, 'adminkey')
            return jsonify({'message': 'you have logged in as the adminstrator',
                    'token': token.decode('utf-8')}), 200

        return jsonify({"message": "username or password is incorrect"}), 400

    def find_user_by_name(self, username):
        query = "SELECT * FROM  users WHERE username = '{}'"
        self.database.cursor.execute(query.format(username))
        row = self.database.cursor.fetchone()
        return row

    def find_user_by_email(self, email):
        query = "SELECT * FROM  users WHERE email = '{}'"
        self.database.cursor.execute(query.format(email))
        row = self.database.cursor.fetchone()
        return row

    def find_user_by_password(self, password):
        query = "SELECT * FROM  users WHERE password = '{}'"
        self.database.cursor.execute(query.format(password))
        row = self.database.cursor.fetchone()
        return row
 