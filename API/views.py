from flask import Flask, jsonify, request
from API.responses import *
# from api.model.user import User
# from api.model.order_request import OrderRequest, lis
# from model.data import *
from API.orders import Parcel
import re

app = Flask(__name__)
parcel = Parcel(1, 1, 'kal@yahoo.com', 'pending', 'cassava', 46, 'Deb', 'kalungi', 'masaka', 'luweero')
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
    item_to_be_shipped = data.get('item_to_be_shipped')
    weight = data.get('weight')
    name_of_sender = data.get('name_of_sender')
    name_of_reciever = data.get('name_of_reciever')
    destination = data.get('destination')
    item_origin = data.get('item_origin')

    
    parcel = { 'order_id' : len(order_list)+1,
        'user_id' :user_id,
        'email':email,
        'status':status,
        'item_to_be_shipped' :item_to_be_shipped,
        'weight' :weight,
        'name_of_sender' :name_of_sender,
        'name_of_reciever' :name_of_reciever,
        'item_origin':item_origin
    }
    if email is None or :
        return jsonify({"message":"Enter your email please"}),200
    if user_id is None:
        return jsonify({"message":"Enter your user_id please"}), 200
    if weight is None:
        return jsonify({"message":"Enter the parcel weight please"}), 200
    if name_of_sender is None:
        return jsonify({"message":"Enter the parcel name_of_sender please"}), 200
    if item_to_be_shipped is None:
        return jsonify({"message":"Enter your item_to_be_shipped please"}), 200
    if name_of_reciever is None:
        return jsonify({"message":"Enter your name_of_reciever please"}), 200
    if destination is None:
        return jsonify({"message":"Enter your destination please"}), 200

    if item_origin is None:
        return jsonify({"message":"Enter your item_origin please"}), 200

  
  
        # itemcurrentlocation :'itemcurrentlocation'
    if not re.match('[^@]+@[^@]+\.[^@]+', data['email']):
        return jsonify({"message": "Invalid email"}), 200

    if type(user_id) == str:
        return jsonify({"message": "The input should be an integer"})


    if type(item_to_be_shipped) == int:
        return jsonify({"message": "The item_to_be_shipped not be should be a be word"})

    specialCharacters = ['$','#','@','!','*']

    if any(char in specialCharacters for char in (data['status'])):
        return jsonify({"message": "You should not input special characters"}), 400

    if data['status'].isspace() or (' ' in data['status']):
        return jsonify({"message": "Field cannot be blank"}), 400
   
    order_list.append(parcel)
    return jsonify({"parcel_order was successfully created":parcel}), 201

@app.route('/api/v1/parcels', methods=['GET'])
def get_parcel():
    if order_list:
        return jsonify({"Parcels":order_list}), 200
    else:
        return jsonify({"message":"No parcels available at the moment"}), 200

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
        else:
            return jsonify({"message": "parcel with that parcel-Id is not available"}),200

@app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
def Cancel_specific_parcel_delivery_order(parcelId):

    for parcel in order_list:
            parcel_dict = parcel.to_dict()
            if parcel_dict['parcel_id'] == parcelId: 
                if parcel_dict['status'] == 'pending':
                    parcel_dict["status"] = "cancelled"
                    return jsonify({"Parcel_delivery_order_cancelled":parcel_dict}), 200
                
            return jsonify({'message':'There is no parcel with that ID'}), 200

