from flask import Flask, jsonify, request
from API.responses import *
# from api.model.user import User
# from api.model.order_request import OrderRequest, lis
# from model.data import *
from API.orders import Parcel
import re

app = Flask(__name__)

# parcel = Parcel(1, 1, 'kal@yahoo.com', 'cassava', 46, 'Deb', 'kalungi', 'masaka', 'deb', 'luweero')
parcel = Parcel(1, 1,'kal@yahoo.com', 'pending')
order_list = []

@app.route('/')
def index():
    return 'welcome to getIt Application. For all you Deliveries'

@app.route('/api/v1/parcels', methods=['POST'])
def send_parcel():
    
    data = request.get_json(force=True)
  
    user_id = data.get('user_id')
    email = data.get('email')
    status = data.get('status')
    # item_to_be_shipped = data.get('item_to_be_shipped', None)
    # weight = data.get('weight', None)
    # name_of_sender = data.get('name_of_sender', None)
    # name_of_reciever = data.get('name_of_reciever', None)
    # destination = data.get('destination', None)
    # username = data.get('username', None)
    # itemcurrentlocation = data.get('itemcurrentlocation', None)

    
    parcel = { 'order_id' : len(order_list)+1,
        'user_id' :user_id,
        'email':email,
        'status':status
        # item_to_be_shipped :'item_to_be_shipped',
        # weight :'weight',
        # name_of_sender :'name_of_sender',
        # name_of_reciever :'name_of_reciever',
        # destination :'destination',
        # username:'username',
        # itemcurrentlocation :'itemcurrentlocation'
    }
    if email is None:
        return jsonify({"message":"Enter your email please"}),400
    if not re.match('[^@]+@[^@]+\.[^@]+', data['email']):
        return jsonify({"message": "Invalid email"}), 400
    if user_id is None:
        return jsonify({"message":"Enter your user_id please"}), 400
    if type(user_id) == str:
        return jsonify({"message": "The user_id should be an integer"})

    specialCharacters = ['$','#','@','!','*']

    if any(char in specialCharacters for char in (data['status'])):
        return jsonify({"message": "status cannot have special characters"}), 400

    if data['status'].isspace() or (' ' in data['status']):
        return jsonify({"message": "Field cannot be blank"}), 400
   
    order_list.append(parcel)
    return jsonify({"parcel successfully created":parcel}), 201

@app.route('/api/v1/parcels', methods=['GET'])
def get_parcel():
    if order_list:
        return jsonify(order_list)
    else:
        return jsonify(empty_list)

@app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
def api_get_sepecific_order(parcelId):
    """this function fetches details
     about a specific order"""
    for i in order_list:
        if i['order_id'] == parcelId:
            return jsonify({"message":i})
        else:
            return jsonify({"message":"the parcel is not available"})

@app.route('/api/v1/users/<int:userId>/parcels', methods=['GET'])
def api_get_all_orders_for_specific_user(userId):
    for parcel in order_list:
        if parcel['user_id'] == userId:
            return jsonify(parcel)

@app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
def Cancel_specific_parcel_delivery_order(parcelId):
    for parcel in order_list:
        if parcel['order_id'] == parcelId:
                # parcel["status"] = "cancelled"
            order_list.pop(parcel)
            return jsonify({"Parcel delivery order cancelled":parcel})
        else:
            return jsonify({'message':'you dont have rights to modify that parcel'})
