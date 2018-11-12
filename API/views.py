from flask import Flask, jsonify, request
# from api.model.responses import *
# from api.model.user import User
# from api.model.order_request import OrderRequest, lis
# from model.data import *
from api.orders import Parcel


app = Flask(__name__)

parcel = Parcel(1, 1, 'kal@yahoo.com', 'cassava', 46, 'Deb', 'kalungi', 'masaka', 'deb', 'luweero')
order_list = []

@app.route('/')
def index():
    return 'welcome to getIt Application. For all you Deliveries'

@app.route('/api/v1/parcels', methods=['POST'])
def send_parcel():
    
    data = request.get_json(force=True)
    order_id = data.get('order_id', None)
    user_id = data.get('user_id', None)
    email = data.get('email', None)



    item_to_be_shipped = data.get('item_to_be_shipped', None)
    weight = data.get('weight', None)
    name_of_sender = data.get('name_of_sender', None)

    name_of_reciever = data.get('name_of_reciever', None)
    destination = data.get('destination', None)
    name_of_sender = data.get('name_of_sender', None)

    username = data.get('username', None)
    itemcurrentlocation = data.get('itemcurrentlocation', None)

    
    parcel = { order_id : 'order_id',
        user_id :'user_id',
        email:'email',
        item_to_be_shipped :'item_to_be_shipped',
        weight :'weight',
        name_of_sender :'name_of_sender',
        name_of_reciever :'name_of_reciever',
        destination :'destination',
        name_of_sender:'name_of_sender',
        username:'username',
        itemcurrentlocation :'itemcurrentlocation'
    }
    order_list.append(parcel)
    return jsonify({"parcel successfully created":parcel})

@app.route('/api/v1/parcels', methods=['GET'])
def get_parcel():
    return jsonify(order_list)

@app.route('/api/v1/parcels/<parcelId>', methods=['GET'])
def api_get_sepecific_order(parcelId):
    """this function fetches details
     about a specific order"""
    for i in order_list:
        if i['order_Id'] == parcelId:
            return jsonify(i)

@app.route('/api/v1/users/<userId>/parcels', methods=['GET'])
def api_get_all_orders_for_specific_user(userId):
    for i in order_list:
        if i['user_Id'] == userId:
            return jsonify(i)

@app.route('/api/v1/parcels/<parcelId>/cancel', methods=['PUT'])
def Cancel_specific_parcel_delivery_order(userId):
    pass







# users = [User("Kataiala", "Kats",
#                    "llkljdf@gmail.com", "Deb", "kwick"), User("maggie", "zoli",
#                    "mGE@gmail.com", "mukasa", "kawa")]

# orders = [Orders( 'kal@gmail', 'mahogany', 21, 'Nairobi', 'Deb', 'Uganda-Mattuga'),  Orders(
#     'bal@gmail', 'chaff', 100, 'Rwanda', 'Deb', 'Malawi')]
# models = Models(users, orders)



# @app.route('/api/v1/signup', methods=['POST'])
# def signup():
#     """signup a new user"""
#     data = request.get_json()
#     first_name = data.get("first_name")
#     last_name = data.get("last_name")
#     email = data.get("email")
#     username = data.get("username")
#     password = data.get("password")
#     if type(first_name) is not str and type(last_name) is not str and \
#             type(email) is not str and type(username) is not str and \
#             type(password) is not str:
#         user = models.search_list(username)
#         if user is None:
#             response = models.create_user(
#                 User(
#                     first_name, last_name, email, username, password)).\
#                 get_dictionary()
         
#             registration_successful["user"] = response
#             return jsonify(registration_successful)

#         else:
#             return jsonify(login_fail), 401
#     else:
#         return jsonify(create_request_fail)


# @app.route('/api/v1/login', methods=['POST'])
# def login():
#         """login"""

#         data = request.get_json(force=True)
#         username = data.get('username', None)
#         password = data.get('password', None)

#         user = models.search_list(username)
#         if user is not None:
#             if user.verify_password(password):
#                 response = user.get_dictionary()
#                 response["token"] = models.generate_auth_token(response)
#                 response["success"] = True
#                 print(str(response))
#                 return jsonify(response)
#             else:
#                 return jsonify(login_fail), 200
#         else:
#             return jsonify(login_fail), 200

# @app.route('/api/v1/parcels', methods=['POST'])
# def send_parcel():
#     """api end point for Creating a parcel delivery order"""
#     data = request.get_json(force=True) 
#     email = data.get('email', None)
#     username = data.get('username', None)
#     item_to_be_shipped = data.get('item_to_be_shipped', None)
#     weight = data.get('weight', None)
#     itemcurrentlocation = data.get('itemcurrentlocation', None)
#     destination = data.get('destination', None)
    

    # if email is not None and item_to_be_shipped \
    #         is not None and username is not None and weight is not None and itemcurrentlocation is not None and destination is not None:
        # requests = Orders(email, item_to_be_shipped, weight, destination, username, itemcurrentlocation)
        # create_request_successful['data'] = models.add_orders(
        #     requests).get_dictionary()
        
        # return jsonify(create_request_successful)
        # orders = Orders
        # orders.create_parcel_order_delivery( order_id, user_id, item_to_be_shipped, weight, name_of_sender, name_of_reciever, destination, itemcurrentlocation)
    # else:
    #     return jsonify(create_request_fail)
        



# @app.route('/api/v1/parcels', methods=['GET'])
# @models.token_required
# def get_parcel(current_user):
#     """function to retrieve all parcel orders by current user"""
#     orders = models.get_all_orders_for_user(
#         current_user.get_username())
    # for order in orders:
    #     if order["order_Id"] == 'bc4ed261-5b67-4b5a-8b51-8d1bdefe5b80':
    # return jsonify(orders)

# @app.route('/api/v1/parcels/<parcelId>', methods=['GET'])
# @models.token_required
# def api_get_sepecific_order(current_user, parcelId):
#     """this function fetches details
#      about a specific parcel order"""
#     req = models.get_a_specific_requests_for_user(parcelId)
#     if req is not None:
#         # create_request_successful['data'] = req
#         return jsonify(create_request_successful)
        
#     else: 
#         return jsonify(request_fail)

# @app.route('/api/v1/users/<user_Id>/parcels', methods=['GET'])
# @models.token_required
# def fetch_all_parcel_orders_by_a_specific_user(username):
#     users = models.get_all_users()
#     print(jsonify(users))
#     req = models.get_all_orders_for_user(username)
#     if req is not None:
#         return jsonify(req)
#     else:
#         return 'not in'

# @app.route('/api/v1/parcels/<parcelId>/cancel', methods=['PUT'])
# @models.token_required
# def counsel_a_specific_parcel_order(current_user,parcelId):

#     """function to modify a specific order"""

#     data = request.get_json(force=True)
#     email = data.get('email', None)
#     item_to_be_shipped = data.get('item_to_be_shipped', None) 
#     weight = data.get('weight', None)
#     owner = data.get('owner', None)
#     destination = data.get('destination', None)
#     itemcurrentlocation = data.get('itemcurrentlocation', None)
#     username = data.get('username', None)


    

#     print(data)
#     if email is not None and item_to_be_shipped \
#             is not None and owner is not None and weight is not None and itemcurrentlocation is not None and destination is not None:
#         requests = Orders(email, item_to_be_shipped, weight, destination, username, itemcurrentlocation, username)
#         mod_req = models.cancel_order(requests)
#         if mod_req is not None:
#             create_request_successful['data'] = mod_req
#             return jsonify(create_request_successful)
#         else:
#             return jsonify(request_fail)
#     else:
#         return jsonify(create_request_fail)

# @app.route('/api/v1/parcelss', methods=['GET'])
# @models.token_required
# def getr_parcel(current_user):
#     """function to retrieve all parcel orders by current user"""
#     orders = models.get_all_orders_for_user(
#         current_user.get_username())
#     for order in orders:
#         return order
        # if order["order_Id"] == '3af4a36a-2afd-452c-aa03-093990f07b38':
        #     return jsonify(order) 
        # else:
        #     return 'no parsel found'


   
