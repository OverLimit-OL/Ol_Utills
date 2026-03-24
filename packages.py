import json

def success_response(data):
    pass

def error_response(message, code):
    pass

def login_required(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(*args)
    return wrapper

def admin_required(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('ali')
    return wrapper