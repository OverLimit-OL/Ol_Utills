from flask import sessions, session, jsonify
import sqlite3, psycopg2
import json, os


def success_response(data):
    pass

def error_response(message, code):
    pass

def login_required(func):
    def login_wrapper(*args, **kwargs):
        if session.get('logged') == True:
            result = func(*args, **kwargs)
            return result
        else:
            return jsonify()
    return login_wrapper

def admin_required(func):
    def admin_wrapper(*args, **kwargs):
        if session.get('admin') == True:
            result = func(*args, **kwargs)
            return result
        else:
            return jsonify()
    return admin_wrapper

def sqlite(database):
    conn = sqlite3.connect(database)
    db = conn.cursor()
