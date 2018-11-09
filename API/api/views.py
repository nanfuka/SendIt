from flask import Flask, request, abort, jsonify

from flask import Flask, jsonify, request
import jwt
from api.models import Models
from api.users import User
from api.orders import Orders
from api.responses import *
app = Flask(__name__)
# api = Api(app)
        

users = [User("Kataala", "Kats",
                   "llkldf@gmail.com", "Deb", "kwick")]

orders = [Orders( 'kal@gmail', 'mahogany', 21, 'Nairobi', 'Deb', 'Uganda-Mattuga'),  Orders(
    'bal@gmail', 'chaff', 100, 'Rwanda', 'Deb', 'Malawi')]
models = Models(users, orders)

@app.route('/')
def index():
    return 'welcome to getIt Application. For all you Deliveries'

@app.route('/api/v1/signup', methods=['POST'])
def signup():
    """signup a new user"""
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    if first_name is not None and last_name is not None and \
            email is not None and username is not None and \
            password is not None:
        user = models.search_list(username)
        if user is None:
            response = models.create_user(
                User(
                    first_name, last_name, email, username, password)).\
                get_dictionary()
         
            registration_successful["user"] = response
            return jsonify(registration_successful)

        else:
            return jsonify(login_fail), 401
    else:
        return jsonify(create_request_fail)


@app.route('/api/v1/login', methods=['POST'])
def login():
        """login"""

        data = request.get_json(force=True)
        username = data.get('username', None)
        password = data.get('password', None)

        user = models.search_list(username)
        if user is not None:
            if user.verify_password(password):
                response = user.get_dictionary()
                response["token"] = models.generate_auth_token(response)
                response["success"] = True
                print(str(response))
                return jsonify(response)
            else:
                return jsonify(login_fail), 200
        else:
            return jsonify(login_fail), 200

@app.route('/api/v1/parcels', methods=['POST'])
@models.token_required
def send_parcel():
    """api end point for Creating a parcel delivery order"""
    data = request.get_json(force=True) 
    email = data.get('email', None)
    username = data.get('username', None)
    item_to_be_shipped = data.get('item_to_be_shipped', None)
    weight = data.get('weight', None)
    itemcurrentlocation = data.get('itemcurrentlocation', None)
    destination = data.get('destination', None)

    if email is not None and item_to_be_shipped \
            is not None and username is not None and weight is not None and itemcurrentlocation is not None and destination is not None:
        requests = Orders(email, item_to_be_shipped, weight, destination, username, itemcurrentlocation, username)
        create_request_successful['data'] = models.add_orders(
            requests).get_dictionary()
        return jsonify({create_request_fail})
    else:
        return jsonify(create_request_fail)


@app.route('/api/v1/parcels', methods=['GET'])
@models.token_required
def get(current_user):
    """function to retrieve all parcel orders"""
    return jsonify(models.get_all_orders_for_user(
        current_user.get_username()))

@app.route('/api/v1/parcels/<parcelId>', methods=['GET'])
@models.token_required
def api_get_sepecific_order(current_user, parcelId):
    """this function fetches details
     about a specific parcel order"""
    req = models.get_a_specific_requests_for_user(parcelId)
    if req is not None:
        create_request_successful['data'] = req
        return jsonify(create_request_successful)
    else:
        return jsonify(request_fail)

# @app.route('/api/v1/orders', methods=['GET'])
# @models.token_required
# def get_all_orders(current_user):
#     """function to retrieve all food orders"""




# api.add_resource(Welcome, '/')

