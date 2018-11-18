from flask import Flask, jsonify, request
from api.model.responses import *
# from api.model.user import User
# from api.model.order_request import OrderRequest
from api.model.data import Userdata
import jwt


app = Flask(__name__)

userdata = Userdata()

@app.route('/')
def api_documentation():
    return "WELCOME TO FAST FOOD FAST APPLICATION"
