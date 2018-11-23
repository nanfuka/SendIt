from flask import Flask, jsonify, request
from functools import wraps
from data import Userdata
# from api import app
# from api.models.data import Userdata
# from flasgger import Swagger, swag_from
# from flask_jwt_extended import (JWTManager,
#                                 jwt_required, 
#                                 create_access_token,
#                                 get_jwt_identity)

app = Flask(__name__)

userdata = Userdata()


# Swagger(app)
    
app.config['USER_KEY'] = 'mylovelykids'
app.config['ADMIN_KEY'] = 'administratorsareannoying'


    # def generate_auth_token(self, user):
    #     """function to generate an auth-token"""
    #     try:
    #         payload = {
    #             'exp': datetime.datetime.utcnow(

    #             ) + datetime.timedelta(minutes=2000),
    #             'iat': datetime.datetime.utcnow(),
    #             'user': user
    #         }
    #         return jwt.encode(
    #             payload,
    #             self.key,
    #             algorithm='HS256'
    #         ).decode('utf-8')
    #     except Exception as e:
    #         return e

# def user_token(func):

#     @wraps(func)
#     def decorated(*args, **kwargs):
#         token = None
#         if "Authorization" in request.headers:
#             token = request.headers['Authorization']
#         else:
#             return jsonify({'message': 'Token is missing'}), 401
#         try:
#             data = jwt.decode(token, app.config['USER_KEY'])
            
#         except:
#             return jsonify({'message': 'Token is missing'}), 401
#         return func(*args, **kwargs)
#     return decorated
# def user_token(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token:
#             return jsonify({'message': 'Token is missing'}), 401
#         try:
#             data=jwt.decode(token[7:], app.config['USER_KEY'])
            
#         except:
#             return jsonify({'message': 'Token is invalid'}), 401
#         return f(data,*args, **kwargs)
#     return decorated


def user_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorisation" in request.headers:
            token = request.headers["Authorization"]
        else:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token[7:], app.config['USER_KEY'])           
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(data, *args, **kwargs)
    return decorated


# def admin_token(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token:
#             return {'message': 'You are not authorised to access this route'}, 403
#         try:
#             jwt.decode(token[7:], app.config['ADMIN_KEY'])
#         except:
#             return {'message': 'Token is invalid'}, 403
#         return f(*args, **kwargs)
#     return decorated


@app.route('/', methods=['GET'])
def index():
    return "WELCOME TO SENDIT COURIEER SERVICES APPLICATION", 200


@app.route('/api/v1/auth/signup', methods=['POST'])
# @swag_from('../docs/signup.yml')
def register_user():
    """signup a new user"""
    return userdata.create_user()


@app.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    """function to login a user. This function returns
    a token which the user uses to access private routes
    """
    return userdata.login_user()


@app.route('/api/v1/users/<userId>/parcels', methods=['GET'])
def find_all_parcels_for_a_particular_user_id(userId):
    """This function returns all parcels for a particular user_id
    """
    return userdata.find_all_parcels_for_a_particular_user_id(userId)


@app.route('/api/v1/parcels/<int:parcel_id>/destination', methods=['PUT'])
def change_destination(parcel_id):
    """function which anable a user to change destination of the parcel
    """
    return userdata.modi_destination(parcel_id)


@app.route('/api/v1/parcels/<parcelId>/status', methods=['PUT'])
def modify_parsel_delivery(parcelId):
    """This route can change a parsels status to cancelled"""
    return userdata.change_status(parcelId)


@app.route('/api/v1/parcels')
@user_token
def view_parcels():
    """This route can retrieve all parcels of a specific user"""
    return userdata.get_all_parcels()


@app.route('/api/v1/parcels', methods=['POST'])
# @swag_from('../Docs/add_item.yml', methods = ['POST'])
def create_parcel():
    """A user can create a parcel from this route"""
    return userdata.create_parcel()


@app.route('/api/v1/parcels/<parcelId>')
def view_specific_parcels(parcelId):
    """This route can Fetch a specific parcel delivery order"""
    return userdata.find_parcel_by_parcel_id(parcelId)


@app.route('/api/v1/parcels/<parcelId>/presentLocation', methods=['PUT'])
def change_presentlocation(parcelId):
    """this function updates the present location 
    of a parcel and only the administrator has rights to modify it"""
    return userdata.modi_present_location(parcelId)
if __name__ == '__main__':
    app.run(debug=True)
   
