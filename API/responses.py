"""Responses for all the reqests made in the app.py"""
registration_successful = {
        'success': True,
        'message': "User Registered Succesfully.",
        }
login_successful = {
        'success': True,
        'message': "Logedin Succesfully.",
        }
login_fail = {
        'success': False,
        'message': "Login Failed."
        }
empty_list = {
        'message':"There are no parsels at the moment"
        }

request_fail = {
        'success': False,
        'message': "Not a valid Request ID."
        }
create_request_fail = {
        'success': False,
        'message': "All fields required."
        }
create_request_successful = {
        'success': True,
        'message': "Your request was submitted successfully.",
        }
