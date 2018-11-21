from flask import Flask, jsonify, request
from api.models.data import Userdata



app = Flask(__name__)

userdata = Userdata()

@app.route('/')
def api_documentation():
    return "WELCOME TO FAST FOOD FAST APPLICATION (CHALLENGE 3)"

@app.route('/api/v1/auth/signup', methods=['POST'])
def register_user():
    """signup a new user"""
    return userdata.create_user()
    