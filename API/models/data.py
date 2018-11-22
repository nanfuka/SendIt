from werkzeug.security import safe_str_cmp
import jwt
import datetime
from flask import jsonify

from functools import wraps
from flask import request
from database_conn import Database
import re

ADMIN_NAME = "admin"
ADMIN_PASSWORD = "password"
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

        specialCharacters = ['$', '#', '@', '!', '*']

        if any(char in specialCharacters for char in (user_data['username'])):
            return {'message': 'username cannot have special characters'}, 400

        elif self.find_user_by_email(user_data['email']):
            return jsonify({'message': 'Email in use, please use another email address'}), 400
        elif user_data['username'].isspace():
            return {'message': 'Field cannot be blank'}, 400

        else:
            query = ("INSERT INTO users(username, email, password)\
            VALUES('{}', '{}', '{}')\
            RETURNING user_id, username, email, password")

        self.database.cursor.execute(query.format(user_data['username'],
                                                  user_data['email'], user_data['password']))

        parcel = {"email": user_data['email'], "username": user_data['username']}

        return jsonify({"message": "user successfully signedup", "user": parcel}), 201

    def find_user_by_username(self, username):
        """
        method that searches the database for 
        a particular username and returns teh row
        where the username is found
        """
        query = "SELECT * FROM  users WHERE username = '{}'"
        self.database.cursor.execute(query.format(username))
        row = self.database.cursor.fetchone()
        return row

    def login_user(self):
        """this function checks against the data 
        stored inn the database to assertain that the 
        password and id belong to the same user before
        logging in
         """
        user_data = request.get_json()
        username = user_data.get('username')
        password = user_data.get('password')

        if not user_data:
            return jsonify({'message': 'All fields are required'}), 400
        if not username or username == " " or username == type(int):
            return jsonify({'message': 'Invalid username'}), 400

        if not password or password == " " or len(password) < 5:
            return jsonify({'message': 'A stronger password  is required'}), 400

        specialCharacters = ['$', '#', '@', '!', '*']

        if any(char in specialCharacters for char in (user_data['username'])):
            return jsonify({'message': 'username cannot have special characters'}), 400
        elif user_data['username'].isspace():
            return jsonify({"message": "Field cannot be blank"}), 400

        query = "SELECT * FROM users WHERE username = '{}'"
        self.database.cursor.execute(query.format(username))
        if self.find_user_by_name(user_data['username']) and self.find_user_by_password(user_data['password']):
            # token = jwt.encode({
            #     'username': user_data['username'],
            #     'exp':
            #     datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            #     }, 'customerkey')
            response = {'message': 'You are successfully logged in',
                        'user': user_data['username']}, 200
            # 'token': token.decode('utf-8'), 'user':user_data}, 200
            return jsonify({"message": response})

        elif user_data['username'] == ADMIN_NAME and user_data['password'] == ADMIN_PASSWORD:
            token = jwt.encode({
                'username': user_data['username'],
                'exp':
                datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, 'adminkey')
            return jsonify({'message': 'you have logged in as the adminstrator',
                            'token': token.decode('utf-8')}), 200

        return jsonify({"message": "username or password is incorrect"}), 400

    def find_user_by_name(self, username):
        """function which searches through the database 
        to assertain that the name passed is present in the database
        """
        query = "SELECT * FROM  users WHERE username = '{}'"
        self.database.cursor.execute(query.format(username))
        row = self.database.cursor.fetchone()
        return row

    def find_user_by_user_id(self, user_id):
        """
        function which searches through the database 
        to assertain that the user_id passed is present in the database
        """
        query = "SELECT * FROM  users WHERE user_id = '{}'"
        self.database.cursor.execute(query.format(user_id))
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

    def create_parcel(self):
        """this function creates a parcel delivery order"""
        user_data = request.get_json()
        user_id = user_data.get('user_id')
        name_of_reciever = user_data.get('name_of_reciever')
        source = user_data.get('source')
        destination = user_data.get('destination')
        status = user_data.get('status')
        presentlocation = user_data.get('presentlocation')

        if not user_data:
            return jsonify({'message': 'All fields are required'}), 400

        if not user_id or user_id == " " or user_id == type(str):
            return jsonify({'message': 'Invalid user_id'}), 400
        if not name_of_reciever or name_of_reciever == " " or name_of_reciever == type(int):
            return jsonify({'message': 'Invalid name_of_reciever'}), 400

        if not source or source == " " or source == type(int):
            return jsonify({'message': 'Invalid source'}), 400

        if not destination or destination == " " or destination == type(int):
            return jsonify({'message': 'invalid destination'}), 400

        if not status or status == " " or status == type(int):
            return jsonify({'message': 'invalid status'}), 400

        query = """
            INSERT INTO parcels(user_id, name_of_reciever, source, destination, status, presentlocation)
            VALUES('{}','{}','{}','{}','{}','{}')
        """
        self.database.cursor.execute(query.format(user_data['user_id'], user_data['name_of_reciever'],
                                                  user_data['source'], user_data['destination'], user_data['status'], user_data['presentlocation']))
        return jsonify({"message": "order successfully created", "parcel": user_data})

    
    def modi_destination(self, parcel_id):
        """this function allows for teh user to change teh destination of teh parcel. however this can only happen if teh parcel is in transit"""
        user_data = request.get_json()
        destination = user_data.get('destination')
        query = "UPDATE parcels SET destination = '{}' WHERE parcel_id = '{}'"
        self.database.cursor.execute(query.format(destination, parcel_id))
        if user_data:
            return jsonify({"current_parsel": user_data, "message": "parsel destination has been updated"}), 200
        return jsonify({"fail": "the parcel_id is not available"})
            
    

    def modi_present_location(self, parcel_id):
        """this function allows for teh user to change teh destination of teh parcel. however this can only happen if teh parcel is in transit"""
        user_data = request.get_json()
        presentlocation = user_data.get('presentlocation')
        query = "UPDATE parcels SET presentlocation = '{}' WHERE parcel_id = '{}'"
        self.database.cursor.execute(query.format(presentlocation, parcel_id))
        if user_data:
            return jsonify({"message": "parsel presentlocations has been updated", "presentlocation": user_data}), 200
        return jsonify({"fail": "the parcel presentlocation has not been modified"})

    def change_status(self, parcelId):
        """this function allows for teh user to change teh destination of teh parcel. however this can only happen if teh parcel is in transit"""
        user_data = request.get_json()
        status = user_data.get('status')
        query = "UPDATE parcels SET status = '{}' WHERE parcel_id = '{}'"
        self.database.cursor.execute(query.format(status, parcelId))
        if user_data:
            return jsonify({"message": "This parcel has been cancelled", "current_parsel": user_data}), 200
        return jsonify({"fail": "the parcel_id has not been modified"})

    # def change_present_parsel_location(self, parcelId):
    #     """this function allows for teh user to change teh destination of teh parcel. however this can only happen if teh parcel is in transit"""
    #     user_data = request.get_json()
    #     status = user_data.get('status')

    #     query = "UPDATE parcels SET present_location = '{}' WHERE parcel_id = '{}'"
    #     self.database.cursor.execute(query.format(status, parcelId))
    #     return jsonify({'message': 'Parsel present location has been updated'}), 200

    def get_all_parcels(self):
        """
        function that returns a history of persels
        """
        query = "SELECT * FROM parcels"
        self.database.cursor.execute(query)
        row = self.database.cursor.fetchall()
        results = []
        if row:
            for parcel in row:
                results.append({
                    'parcel_id': parcel[0],
                    'user_id': parcel[1],
                    'name_of_reciever': parcel[2],
                    'source': parcel[3],
                    'destination': parcel[4],
                    'status': parcel[5]

                })
            return jsonify({"View all parcels": results})
        else:
            return jsonify({'parcels': 'No parcels found'}), 404

    def find_parcel_by_parcel_id(self, parcel_id):
        query = "SELECT * FROM  parcels WHERE parcel_id = '{}'"
        self.database.cursor.execute(query.format(parcel_id))
        row = self.database.cursor.fetchall()
        results = []
        if row:
            for parcel in row:
                results.append({
                    'parcel_id': parcel[0],
                    'user_id': parcel[1],
                    'name_of_reciever': parcel[2],
                    'source': parcel[3],
                    'destination': parcel[4],
                    'status': parcel[5]

                })
            return jsonify({"parcel": results})
        return jsonify({"fail": "the parcel is not available"})

    def find_all_parcels_for_a_particular_user_id(self, user_id):
        query = "SELECT * FROM  parcels WHERE user_id = '{}'"
        self.database.cursor.execute(query.format(user_id))
        row = self.database.cursor.fetchall()
        results = []
        if row:
            for parcel in row:
                results.append({
                    'parcel_id': parcel[0],
                    'user_id': parcel[1],
                    'name_of_reciever': parcel[2],
                    'source': parcel[3],
                    'destination': parcel[4],
                    'status': parcel[5]

                })
            return jsonify({"parcels": results})
        return jsonify({"fail": "the user_id you entered is not available"})
                    

