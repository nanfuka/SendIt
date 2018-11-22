import string  # pragma: no cover
import re
from numbers import Number
from datetime import datetime  # pragma: no cover
from flask import Flask, jsonify  # pragma: no cover

app = Flask(__name__)

from api.views import *


class Validator:  # pragma: no cover

    def is_empty(str):
        if len(str) == 0:
            return True
        return False

    @staticmethod
    def validate_name(name):
        if name and len(name) < 3:
            return True
        return False

    def is_space(str):
        if len(str) == 0:
            return True
        return False
    
    def is_email(item):
        if item != r'[\w\.-]+@[\w\.-]+':
            raise Exception("please enter a valid email!!")

    def doesnot_exist(str):
        if not str or len(str) == 0:
            return jsonify({
                'message': 'Sorry! Item should at least have three characters'
            }), 400

    def is_not_integer(int):
        if not int:
            return jsonify({
                'message': 'Sorry item should be an integer'
            }), 400

    def password(item):
        if not item:
            raise Exception("Field can't be empty")
        if len(item) < 8 or len(item) > 12:
            raise Exception(
                "Weak password. Password must be 8 characters long")
        if not re.search(r'[0-9]', item):
            raise Exception(
                'Weak password. Password should have atleast one integer')
        if item.isupper() or item.isdigit():
            raise Exception('Very Weak password')

    def get_timestamp():
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))