from flask import sessions, session
import json


def success_response(data):
    pass

def error_response(message, code):
    pass

def login_required(func):
    def wrapper(*args, **kwargs):
        if session.get('logged') == True:
            result = func(*args, **kwargs)
            return result
        else:
            return 'shit'
    return wrapper

def admin_required(func):
    def wrapper(*args, **kwargs):
        if session.get('admin') == True:
            result = func(*args, **kwargs)
            return result
        else:
            return 'shit'
    return wrapper