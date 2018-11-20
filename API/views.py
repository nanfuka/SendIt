from flask import Flask, jsonify, request

from API.orders import Parcel

import re


app = Flask(__name__)


parcel = Parcel(1, 1, 'kal@yahoo.com', 'pending', 'cassava',
                46, 'Deb', 'kalungi', 'masaka', 'luweero')


order_list = []


@app.route('/')
def api_documentation():

    return "WELCOME TO SEND_IT APP, THE SOLUTION TO ALL YOUR COUREER SERVICES"


@app.route('/api/v1/parcels', methods=['POST'])
def send_parcel():
    """function to create a new parcel. A user is expected to enter all

     their credentials in their valid format

    """

    specialCharacters = ['$', '#', '@', '!', '*']

    data = request.get_json(force=True)

    user_id = data.get('user_id')

    email = data.get('email')

    status = data.get('status')

    item_to_be_shipped = data.get('item_to_be_shipped')

    weight = data.get('weight')

    name_of_reciever = data.get('name_of_reciever')

    destination = data.get('destination')

    item_origin = data.get('item_origin')

    parcel = {'order_id': len(order_list)+1,

              'user_id': user_id,

              'email': email,

              'status': status,

              'item_to_be_shipped': item_to_be_shipped,

              'weight': weight,

              'name_of_reciever': name_of_reciever,

              'item_origin': item_origin,

              'destination': destination



              }

    if user_id is None:

        return jsonify({"message": "Enter your user_id please"}), 400

    elif isinstance(user_id, str):

        return jsonify({"message": "The input should be a number"}), 400

    elif email is None:

        return jsonify({"message": "Enter your email please"}), 400

    elif not re.match('[^@]+@[^@]+\.[^@]+', data['email']):

        return jsonify({"message": "Invalid email"}), 400

    elif item_to_be_shipped is None:

        return jsonify(
            {"message": "Enter your item_to_be_shipped please"}), 400

    elif isinstance(item_to_be_shipped, int):

        return jsonify({"message": "The input should be string"}), 400

    elif weight is None:

        return jsonify({"message": "Enter the parcel weight please"}), 400

    elif isinstance(weight, str):

        return jsonify({"message": "The input should be a number"}), 400

    elif item_origin is None:

        return jsonify({"message": "Enter your item_origin please"}), 400

    elif isinstance(weight, str):

        return jsonify({"message": "The input should be a number"}), 400

    elif destination is None:

        return jsonify({"message": "Enter your destination please"}), 400

    elif isinstance(destination, int):

        return jsonify({"message": "The input should be a string"}), 400

    elif name_of_reciever is None:

        return jsonify({"message": "Enter your name_of_reciever please"}), 400

    elif isinstance(name_of_reciever, int):

        return jsonify({"message": "The input should be a string"}), 400

    elif any(char in specialCharacters for char in (data['name_of_reciever'])):

        return jsonify({"message": "Enter a valid name of reciever"}), 400

    elif any(char in specialCharacters for char in (data['destination'])):

        return jsonify({"message": "Enter a valid destination"}), 400

    elif any(char in specialCharacters for char in (
            data['item_to_be_shipped'])):

        return jsonify({"message": "Enter a valid item_to_be_shipped"}), 400

    elif data['item_to_be_shipped'].isspace() or \
            (' ' in data['item_to_be_shipped']):

        return jsonify({"message": "item to be shipped cannot be blank"}), 400

    elif data['name_of_reciever'].isspace()\
            or (' ' in data['name_of_reciever']):

        return jsonify({"message": "name of reciever cannot be blank"}), 400

    elif data['destination'].isspace() or (' ' in data['destination']):

        return jsonify({"message": "destination cannot be blank"}), 400

    elif data['item_origin'].isspace() or (' ' in data['item_origin']):

        return jsonify({"message": "item origin cannot be blank"}), 400

    order_list.append(parcel)

    return jsonify({"parcel_order was successfully created": parcel}), 201


@app.route('/api/v1/parcels', methods=['GET'])
def get_parcel():

    if order_list:

        """using this route a user be able to view 
        all of his parcel order history
        """

        return jsonify({"Parcels": order_list}), 400

    else:

        return jsonify({"message": "No parcels available at the moment"}), 200


@app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
def api_get_sepecific_order(parcelId):
    """this function fetches all the percel order details about a specific user

    """

    order = [order for order in order_list if order['order_id'] == parcelId]

    if order:

        return jsonify({"order": order[0]})

    else:

        return jsonify({'message': "the parcel_id is not available"})


@app.route('/api/v1/users/<int:userId>/parcels', methods=['GET'])
def api_get_all_orders_for_specific_user(userId):
    """an admin can vew all orders of a specific user"""

    order = [order for order in order_list if order['user_id'] == userId]

    if order:

        return jsonify({"order": order[0]})

    else:

        return jsonify({'message': "the user_id is not available"})


@app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
def Cancel_specific_parcel_delivery_order(parcelId):
    """Using the put method, a user can retrieve and order and modify

     its status. however this can only be done if the 
     current status is "in transit"

    """

    data = request.get_json(['status'])

    specific_order = [
        order for order in order_list if order['order_id'] == parcelId]

    specific_order[0]['status'] = data

    if data:

        return jsonify({"success": specific_order}), 200

    return jsonify({"message": "The order_id is invalid"}), 400
