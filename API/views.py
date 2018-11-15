from flask import Flask, jsonify, request
from API.orders import Parcel
import re
from API.users import User
from API.data import DataStore
from API.responses import *

app = Flask(__name__)
# parcel = Parcel(1, 1, 'kal@yahoo.com', 'pending', 'cassava', 46, 'Deb', 'kalungi', 'masaka', 'luweero')
parcel = Parcel(1, 1, 'kal@yahoo.com')
order_list = []
temp_users = [User("Nsubuga", "Kalungiowak",
                   "llkldf@gmail.com", "Deb", "boosiko", True)]
data_store = DataStore(temp_users)
@app.route('/api/v1/login', methods=['POST'])
def login():
    """Auser can login to the app using this route. after logging 
    in, a user will get a token which he will use to access other private routes
    """
    data = request.get_json(force=True)
    username = data.get('username', None)
    password = data.get('password', None)

    user = data_store.search_list(username)
    if user is not None:
        if user.verify_password(password):
            response = user.get_dictionary()
            response["token"] = data_store.generate_auth_token(response)
            response["success"] = True
            print(str(response))
            return jsonify(response)
        else:
            return jsonify({"message:" "wrong input values"}), 200
    else:
        return jsonify({"message:" "please register with the app first"}), 200


@app.route('/api/v1/register', methods=['POST'])
def register_user():
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
        user = data_store.search_list(username)
        if user is None:
            response = data_store.create_user(
                User(
                    first_name, last_name, email, username, password)).\
                get_dictionary()
            response["token"] = data_store.generate_auth_token(response)
            registration_successful["user"] = response
            return jsonify(registration_successful)

        else:
            return jsonify(login_fail), 401
    else:
        return jsonify(create_request_fail)





@app.route('/')
def index():
    """api for the index route"""
    return 'welcome to getIt Application. For all you Deliveries'

@app.route('/api/v1/parcels', methods=['POST'])
# @data_store.token_required
def send_parcel():
    """A user can create a parsel delivery order by filling all the required fileds"""
    
    
    data = request.get_json(force=True)
  
    user_id = data.get('user_id')
    email = data.get('email')
    # status = data.get('status')
    # item_to_be_shipped = data.get('item_to_be_shipped')
    # weight = data.get('weight')
    # name_of_sender = data.get('name_of_sender')
    # name_of_reciever = data.get('name_of_reciever')
    # destination = data.get('destination')
    # item_origin = data.get('item_origin')

    
    parcel = { 'order_id' : len(order_list)+1,
        'user_id' :user_id,
        'email':email,
        # 'status':status,
        # 'item_to_be_shipped' :item_to_be_shipped,
        # 'weight' :weight,
        # 'name_of_sender' :name_of_sender,
        # 'name_of_reciever' :name_of_reciever,
        # 'item_origin':item_origin
    }
    if user_id is None:
        return jsonify({"message":"Enter your user_id please"}), 200
    if type(user_id) == str:
        return jsonify({"message": "The input should be a number"}),200
    if email is None:
        return jsonify({"message":"Enter your email please"}),200
    if not re.match('[^@]+@[^@]+\.[^@]+', data['email']):
        return jsonify({"message": "Invalid email"}), 200
    # if name_of_sender is None:
    #     return jsonify({"message":"Enter the parcel name_of_sender please"}), 200    
    # if item_to_be_shipped is None:
    #     return jsonify({"message":"Enter your item_to_be_shipped please"}), 200    
    # if weight is None:
    #     return jsonify({"message":"Enter the parcel weight please"}), 200
    # if type(weight) == str:
    #     return jsonify({"message": "The input should be a number"}),200
    # if item_origin is None:
    #     return jsonify({"message":"Enter your item_origin please"}), 200    
    # if destination is None:
    #     return jsonify({"message":"Enter your destination please"}), 200

    # if name_of_reciever is None:
    #     return jsonify({"message":"Enter your name_of_reciever please"}), 200

    # # if type(item_to_be_shipped) == int:
    # #     return jsonify({"message": "The item_to_be_shipped not be should be a be word"}),200

    # specialCharacters = ['$','#','@','!','*']

    # if any(char in specialCharacters for char in (data['status'])):
    #     return jsonify({"message": "Enter a valid status"}), 200

    # if any(char in specialCharacters for char in (data['name_of_sender'])):
    #     return jsonify({"message": "Enter a valid name of sender"}), 200

    # if any(char in specialCharacters for char in (data['name_of_reciever'])):
    #     return jsonify({"message": "Enter a valid name of reciever"}), 200

    # if any(char in specialCharacters for char in (data['destination'])):
    #     return jsonify({"message": "Enter a valid destination"}), 200

    # if any(char in specialCharacters for char in (data['item_to_be_shipped'])):
    #     return jsonify({"message": "Enter a valid item_to_be_shipped"}), 200
 

    # if data['item_to_be_shipped'].isspace() or (' ' in data['item_to_be_shipped']):
    #     return jsonify({"message": "item to be shipped cannot be blank"}), 200

    # if data['name_of_sender'].isspace() or (' ' in data['name_of_sender']):
    #     return jsonify({"message": "name of sender cannot be blank"}), 200

    # if data['name_of_reciever'].isspace() or (' ' in data['name_of_reciever']):
    #     return jsonify({"message": "name of reciever cannot be blank"}),200 
        
    # if data['destination'].isspace() or (' ' in data['destination']):
    #     return jsonify({"message": "destination cannot be blank"}), 200

    # if data['item_origin'].isspace() or (' ' in data['item_origin']):
    #     return jsonify({"message": "item origin cannot be blank"}), 200

    # if data['status'].isspace() or (' ' in data['status']):
    #     return jsonify({"message": "Field cannot be blank"}), 200
   
        order_list.append(parcel)

    return jsonify({"parcel_order was successfully created":parcel}), 201

@app.route('/api/v1/parcels', methods=['GET'])
def get_parcel():
    if order_list:
        """using this route a user be able to view all of his parcel order history"""
        return jsonify({"Parcels":order_list}), 200
    else:
        return jsonify({"message":"No parcels available at the moment"}), 200

@app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
def api_get_sepecific_order(parcelId):
    """this function fetches all the percel order details about a specific user
    """
    for i in order_list:
        if i['order_id'] == parcelId:
            return jsonify({"message":i})
        else:
            return jsonify({"message":"the parcel is not available"})

@app.route('/api/v1/users/<int:userId>/parcels', methods=['GET'])
def api_get_all_orders_for_specific_user(userId):
    """an admin can vew all orders of a specific user"""
    for parcel in order_list:
        if parcel['user_id'] == userId:
            return jsonify(parcel)
        else:
            return jsonify({"message": "parcel with that parcel-Id is not available"}),200

@app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
def Cancel_specific_parcel_delivery_order(parcelId):
    """Using the put method, a user can retrieve and order and modify
     its status. however this can only be done if the current status is "in transit"
    """
    for parcel in order_list:
            parcel_dict = parcel.to_dict()
            if parcel_dict['parcel_id'] == parcelId: 
                if parcel_dict['status'] == 'pending':
                    parcel_dict["status"] = "cancelled"
                    return jsonify({"Parcel_delivery_order_cancelled":parcel_dict}), 200
                
                return jsonify({'message':'you only cancel a persel in transit'}), 200

