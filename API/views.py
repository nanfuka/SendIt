from flask import Flask, jsonify, request

from api.orders import Parcel


app = Flask(__name__)


parcel = Parcel(1, 1, 'kal@yahoo.com', 'pending', 'cassava',
                46, 'Deb', 'kalungi', 'masaka', 'luweero')


order_list = []


@app.route('/')
def api_documentation():
    """function that returns a welcome note to the index page"""
    return "WELCOME TO SEND_IT APP, THE SOLUTION TO ALL YOUR COUREER SERVICES"


@app.route('/api/v1/parcels', methods=['POST'])
def send_parcel():
    """function to create a new parcel. A user is expected to enter all

     their credentials in their valid format

    """

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

    if email is None:

        return jsonify({"message": "Enter your email please"}), 400
    if item_to_be_shipped is None:

        return jsonify(
            {"message": "Enter your item_to_be_shipped please"}), 400

    if weight is None:

        return jsonify({"message": "Enter your weight please"}), 400

    if name_of_reciever is None:

        return jsonify({"message": "Enter your name_of_reciever please"}), 400

    if item_origin is None:

        return jsonify({"message": "Enter your item_origin please"}), 400

    if destination is None:

        return jsonify({"message": "Enter your destination please"}), 400

    if isinstance(user_id, str) or user_id == " ":

        return jsonify({"message": "The input should be a number"}), 400

    if isinstance(status, int) or status == " ":

        return jsonify({"message": "The input should be a string"}), 400

    if isinstance(item_to_be_shipped, int) or item_to_be_shipped == " ":

        return jsonify({"message": "The input should be a string"}), 400

    if isinstance(weight, str) or weight == " ":

        return jsonify({"message": "The input should be a number"}), 400

    if isinstance(name_of_reciever, int) or name_of_reciever == " ":

        return jsonify({"message": "The input should be a string"}), 400

    if isinstance(item_origin, int) or item_origin == " ":

        return jsonify({"message": "The input should be a string"}), 400

    if isinstance(destination, int) or user_id == " ":

        return jsonify({"message": "The input should be a string"}), 400

    special_characters = ['$', '#', '@', '!', '*']

    if any(char in special_characters for char in data['username']):
        return {'message': 'username cannot have special characters'}, 400

    if any(char in special_characters
           for char in (data['item_to_be_shipped'])):
        return {'message':
                'item_to_be_shipped cannot have special characters'}, 400

    if any(char in special_characters for char in (data['destination'])):
        return {'message': 'destination cannot have special characters'}, 400

    if any(char in special_characters for char in (data['item_origin'])):
        return {'message': 'item_origin cannot have special characters'}, 400

    if any(char in special_characters for char in (data['name_of_reciever'])):
        return {'message':
                'name_of_reciever cannot have special characters'}, 400

    if email is None:

        return jsonify({"message": "Invalid email"}), 400

    if item_to_be_shipped is None:

        return jsonify(
            {"message": "Enter your item_to_be_shipped please"}), 400

    if isinstance(item_to_be_shipped, int):

        return jsonify({"message": "The input should be string"}), 400

    if weight is None:

        return jsonify({"message": "Enter the parcel weight please"}), 400

    if isinstance(weight, str):

        return jsonify({"message": "The input should be a number"}), 400

    if item_origin is None:

        return jsonify({"message": "Enter your item_origin please"}), 400

    if isinstance(weight, str):

        return jsonify({"message": "The input should be a number"}), 400

    if destination is None:

        return jsonify({"message": "Enter your destination please"}), 400

    if isinstance(destination, int):

        return jsonify({"message": "The input should be a string"}), 400

    if name_of_reciever is None:

        return jsonify({"message": "Enter your name_of_reciever please"}), 400

    if isinstance(name_of_reciever, int):

        return jsonify({"message": "The input should be a string"}), 400

    if data['item_to_be_shipped'].isspace() or \
            (' ' in data['item_to_be_shipped']):

        return jsonify({"message": "item to be shipped cannot be blank"}), 400

    if data['name_of_reciever'].isspace()\
            or (' ' in data['name_of_reciever']):

        return jsonify({"message": "name of reciever cannot be blank"}), 400

    if data['destination'].isspace() or (' ' in data['destination']):

        return jsonify({"message": "destination cannot be blank"}), 400

    if data['item_origin'].isspace() or (' ' in data['item_origin']):

        return jsonify({"message": "item origin cannot be blank"}), 400

    order_list.append(parcel)

    return jsonify({"parcel_order was successfully created": parcel}), 201


@app.route('/api/v1/parcels', methods=['GET'])
def get_parcel():
    """using this route a user be able to view 
       all of his parcel order history
    """

    if order_list:

        return jsonify({"Parcels": order_list}), 400

    return jsonify({"message": "No parcels available at the moment"}), 200


@app.route('/api/v1/parcels/<int:parcel_id>', methods=['GET'])
def api_get_sepecific_order(parcel_id):
    """this function fetches all the percel order details about a specific user

    """

    order = [order for order in order_list if order['order_id'] == parcel_id]

    if order:

        return jsonify({"order": order[0]})

    return jsonify({'message': "the parcel_id is not available"})


@app.route('/api/v1/users/<int:user_id>/parcels', methods=['GET'])
def api_get_all_orders_for_specific_user(user_id):
    """an admin can vew all orders of a specific user"""

    order = [order for order in order_list if order['user_id'] == user_id]

    if order:

        return jsonify({"order": order})

    return jsonify({'message': "the user_id is not available"})


@app.route('/api/v1/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_specific_parcel_delivery_order(parcel_id):
    """Using the put method, a user can retrieve and order and modify

     its status. however this can only be done if the 
     current status is "in transit"

    """

    data = request.get_json(['status'])

    specific_order = [
        order for order in order_list if order['order_id'] == parcel_id]

    specific_order[0]['status'] = data

    if data:

        return jsonify({"success": specific_order}), 200

    return jsonify({"message": "The order_id is invalid"}), 400
