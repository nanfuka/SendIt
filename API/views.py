from flask import Flask, jsonify, request
from API.orders import Parcel
import re
from API.users import User
from API.data import DataStore
from API.responses import *


app = Flask(__name__)

parcel = Parcel(1, 1, 'kal@yahoo.com', 'pending', 'cassava', 46, 'Deb', 'kalungi', 'masaka', 'luweero')
# parcel = Parcel(1, 1, 'kal@yahoo.com')
order_list = []
temp_users = [User("Nsubuga", "Kalungiowak",
                   "llkldf@gmail.com", "Deb", "boosiko", True)]
data_store = DataStore(temp_users)


@app.route('/')
def api_documentation():
    return "WELCOME TO SEND_IT APP, THE SOLUTION TO ALL YOUR COUREER SERVICES"

# @app.route('/api/v1/register', methods=['POST'])
# def register_user():
#     """signup a new user with the application to that they
#      can be able to access its servises
#      """
#     data = request.args
#     first_name = data.get("first_name")
#     last_name = data.get("last_name")
#     email = data.get("email")
#     username = data.get("username")
#     password = data.get("password")
#     if first_name is not None and last_name is not None and \
#             email is not None and username is not None and \
#             password is not None:
#         user = data_store.search_list(username)
#         if user is None:
#             response = data_store.create_user(
#                 User(
#                     first_name, last_name, email, username, password)).\
#                 get_dictionary()
#             response["token"] = data_store.generate_auth_token(response)
#             registration_successful["user"] = response
#             return jsonify(registration_successful)

#         else:
#             return jsonify(login_fail), 401
#     else:
#         return jsonify(create_request_fail)

# @app.route('/api/v1/login', methods=['POST'])
# def login():
#     """login"""

#     data = request.get_json(force=True)
#     username = data.get('username', None)
#     password = data.get('password', None)

#     user = data_store.search_list(username)
#     if user is not None:
#         if user.verify_password(password):
#             response = user.get_dictionary()
#             response["token"] = data_store.generate_auth_token(response)
#             response["success"] = True
#             print(str(response))
#             return jsonify(response)
#         else:
#             return jsonify(login_fail), 200
#     else:
#         return jsonify(login_fail), 200



@app.route('/api/v1/parcels', methods=['POST'])
# @data_store.token_required
def send_parcel():
    """A user can create a parsel delivery order by filling all the required fileds"""
    
    specialCharacters = ['$','#','@','!','*']
    data = request.get_json(force=True)
  
    user_id = data.get('user_id')
    email = data.get('email')
    status = data.get('status')
    item_to_be_shipped = data.get('item_to_be_shipped')
    weight = data.get('weight')
    name_of_reciever = data.get('name_of_reciever')
    destination = data.get('destination')
    item_origin = data.get('item_origin')

    
    parcel = { 'order_id' : len(order_list)+1,
        'user_id' :user_id,
        'email':email,
        'status':status,
        'item_to_be_shipped' :item_to_be_shipped,
        'weight' :weight,
#        
        'name_of_reciever' :name_of_reciever,
        'item_origin':item_origin,
        'destination': destination
        
    }
    if user_id is None:
        return jsonify({"message":"Enter your user_id please"}), 200
    elif isinstance(user_id, str):
        return jsonify({"message": "The input should be a number"}),200
    elif email is None:
        return jsonify({"message":"Enter your email please"}),200
    elif not re.match('[^@]+@[^@]+\.[^@]+', data['email']):
        return jsonify({"message": "Invalid email"}), 200
   
    elif item_to_be_shipped is None:
        return jsonify({"message":"Enter your item_to_be_shipped please"}), 200 

    elif isinstance(item_to_be_shipped, int):
        return jsonify({"message": "The input should be string"}),200   
    elif weight is None:
        return jsonify({"message":"Enter the parcel weight please"}), 200
    elif isinstance(weight, str):
        return jsonify({"message": "The input should be a number"}),200
    elif item_origin is None:
        return jsonify({"message":"Enter your item_origin please"}), 200   
    elif isinstance(weight, str):
        return jsonify({"message": "The input should be a number"}),200 
    elif destination is None:
        return jsonify({"message":"Enter your destination please"}), 200
    elif isinstance(destination, int):
        return jsonify({"message": "The input should be a string"}),200

    elif name_of_reciever is None:
        return jsonify({"message":"Enter your name_of_reciever please"}), 200
    elif isinstance(name_of_reciever, int):
        return jsonify({"message": "The input should be a string"}),200


    elif any(char in specialCharacters for char in (data['name_of_reciever'])):
        return jsonify({"message": "Enter a valid name of reciever"}), 200

    elif any(char in specialCharacters for char in (data['destination'])):
        return jsonify({"message": "Enter a valid destination"}), 200

    elif any(char in specialCharacters for char in (data['item_to_be_shipped'])):
        return jsonify({"message": "Enter a valid item_to_be_shipped"}), 200
 

    elif data['item_to_be_shipped'].isspace() or (' ' in data['item_to_be_shipped']):
        return jsonify({"message": "item to be shipped cannot be blank"}), 200


    elif data['name_of_reciever'].isspace() or (' ' in data['name_of_reciever']):
        return jsonify({"message": "name of reciever cannot be blank"}),200 
        
    elif data['destination'].isspace() or (' ' in data['destination']):
        return jsonify({"message": "destination cannot be blank"}), 200

    elif data['item_origin'].isspace() or (' ' in data['item_origin']):
        return jsonify({"message": "item origin cannot be blank"}), 200
  
    order_list.append(parcel)

    return jsonify({"parcel_order was successfully created":parcel}), 201

@app.route('/api/v1/parcels', methods=['GET'])
# @data_store.token_required
def get_parcel():
    if order_list:
        """using this route a user be able to view all of his parcel order history"""
        return jsonify({"Parcels":order_list}), 200
    else:
        return jsonify({"message":"No parcels available at the moment"}), 200

@app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
# @data_store.token_required
def api_get_sepecific_order(parcelId):

    """this function fetches all the percel order details about a specific user
    """
    order = [order for order in order_list if order['order_id']==parcelId]
    if order:
        return jsonify({"order":order[0]})
    else:
        return jsonify({'message': "the parcel_id is not available"})



@app.route('/api/v1/users/<int:userId>/parcels', methods=['GET'])

def api_get_all_orders_for_specific_user(userId):
    """an admin can vew all orders of a specific user"""
    # for order in order_list:
    #     if order['user_id'] == userId:
         
    #         return jsonify(order)
        
    #     else:
              
    #         return jsonify({"message":"the user is not available"})
    order = [order for order in order_list if order['user_id']==userId]
    if order:
        return jsonify({"order":order[0]})
    else:
        return jsonify({'message': "the user_id is not available"})

@app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
# @data_store.token_required
def Cancel_specific_parcel_delivery_order(parcelId):
    """Using the put method, a user can retrieve and order and modify
     its status. however this can only be done if the current status is "in transit"
       
    """
    data = request.get_json(['status'])  
    specific_order=[order for order in order_list if order['order_id']==parcelId]
    specific_order[0]['status'] = data 
    if data:   
        return jsonify({"success": specific_order})
    return jsonify({"message":"The order_id is invalid"})
