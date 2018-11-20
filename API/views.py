from flask import Flask, jsonify, request

# from api.model.user import User
# from api.model.order_request import OrderRequest
from api.model.data import Userdata
import jwt
from functools import wraps


app = Flask(__name__)
app.config['USER_KEY'] = 'mylovelykids'
app.config['ADMIN_KEY'] = 'administratorsareannoying'
app.config['ADMIN'] = 'admin'
app.config['ADMIN-PASSWORD'] = 'adminpassword'

userdata = Userdata()

def user_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return {'message': 'Token is missing'}, 403
        try:
            jwt.decode(token[7:], app.config['USER_KEY'])
        except:
            return {'message': 'Token is invalid'}, 403
        return f(*args, **kwargs)
    return decorated


def admin_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return {'message': 'You are not authorised to access this route'}, 403
        try:
            jwt.decode(token[7:], app.config['ADMIN_KEY'])
        except:
            return {'message': 'Token is invalid'}, 403
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def api_documentation():
    return "WELCOME TO SEND_IT APPLICATION"

@app.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    """signup a new user"""
    return userdata.create_user()

@app.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    """Auser can login into the app by entering their username and matching password which they used at registration"""
    return userdata.login_user()

@app.route('/api/v1/parcels/<parcelId>/destination', methods=['PUT'])
def change_destination(parcelId):
    """This function enables the user to change the percel destination"""
    return userdata.modify_destination(parcelId)

@app.route('/api/v1/parcels', methods=['POST'])
def create_persel():
    return userdata.create_parcel()

@app.route('/api/v1/parcels', methods=['GET'])
def get_parcel():
    return userdata.get_all_parcels()

@app.route('/api/v1/<parcelId>/status', methods=['PUT'])
def change_parsel_status(parcelId):
    return userdata.change_status(parcelId)

@app.route('/api/v1/<parcelId>presentlocation', methods=['PUT'])
def change_present_location(parcelId):
    return userdata.change_present_parsel_location(parcelId)
