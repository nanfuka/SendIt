from flask import Flask, jsonify, request
from api.models.data import Userdata
# from flasgger import Swagger, swag_from



app = Flask(__name__)
# api = Api(app)
# swagger = Swagger(app, template = {"info":{{
#     "title": "sendIT API",
#     "description": "Developed by Kalungi Deborah"
# }})

userdata = Userdata()

@app.route('/')
def index():
    return "WELCOME TO FAST FOOD FAST APPLICATION (CHALLENGE 3)",201

@app.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    """signup a new user"""
    return userdata.create_user()

@app.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    """function to login a user. This function returns
    a token which the user uses to access private routes
    """
    return userdata.login_user()

@app.route('/api/v1/auth/parcels')
def view_parcels():
    """This route can retrieve all parcels of a specific user"""
    return userdata.get_all_parcels()

@app.route('/api/v1/auth/parcels', methods=['POST'])
# @swag_from('../Docs/add_item.yml', methods = ['POST'])
def create_parcel():
    """A user can create a parcel from this route"""
    return userdata.create_parcel()

@app.route('/api/v1/parcels/<parcelId>')
def view_specific_parcels(parcelId):
    """This route can Fetch a specific parcel delivery order"""
    return userdata.find_parcel_by_parcel_id(parcelId)

@app.route('/api/v1/parcels/<parcelId>/status', methods = ['PUT'])
def modify_parsel_delivery(parcelId):
    """This route can change a parsels status to cancelled"""
    return userdata.change_status(parcelId)

@app.route('/api/v1/parcels/<parcelId>/destination', methods = ['PUT'])
def change_destination(parcelId):
    """this function modifies teh current destination"""
    return userdata.modify_destination(parcelId)

@app.route('/api/v1/parcels/<parcelId>/presentLocation', methods = ['PUT'])
def change_presentlocation(parcelId):
    """this function updates the present location 
    of a parcel and only the administrator has rights to modify it"""
    return userdata.modify_present_location(parcelId)


    