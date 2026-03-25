from flask import sessions, session, jsonify, request
import json, os
import re
import uuid
import time
from functools import wraps

class val:

    password_regex = r"^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$"
    email_regex = r"^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$"
    phone_regex= r"/(?:([+]\d{1,4})[-.\s]?)?(?:[(](\d{1,3})[)][-.\s]?)?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,9})/g"

    @staticmethod
    def chk_p(password):
        # Checks for password containing at least 1 Upper case, 1 lower case, 1 digit and 1 special character,
        # all together with a length of at least 8. (This pattern allows any order of the requried elements,
        # other than what was been distributed here before)

        __p = re.search(val.password_regex, password)
        if __p:
            return True
    
    @staticmethod
    def chk_e(email):
        # Email address compliant with RFC2822

        __e = re.search(val.email_regex, email)
        if __e:
            return True
    
    @staticmethod
    def chk_ph(phone):
        # Detects most of the phone numbers all over the world

        __ph = re.search(val.phone_regex, phone)
        if __ph:
            return True

class res:
    # Standardized response format for API responses

    def success_response(data):
        pass

    def error_response(message, code):
        pass

class Connections:

    @staticmethod
    def sqlite(database):
        import sqlite3
        # Connects to a SQLite database and returns a cursor object for executing queries

        conn = sqlite3.connect(database)
        db = conn.cursor()
        return conn, db

    @staticmethod
    def postgresql(database, user, password, host):
        import psycopg2
        # Connects to a PostgreSQL database and returns a cursor object for executing queries

        conn = psycopg2.connect(database=database, user=user, password=password, host=host)
        db = conn.cursor()
        return conn, db
    
    @staticmethod
    def C_redis(host='localhost', port=6379, password=None, socket_timeout=5):
        import redis
        # Create redis Connection
        
        try:
            r = redis.Redis(
                host=host,
                port=port,
                password=password,
                decode_responses=True,
                socket_timeout=socket_timeout,
                protocol=3
            )
            return r
        except Exception as e:
            return str(e)

class req:

    @staticmethod
    def login_required(f):
        # Decorator to check if the user is logged in before allowing access to a route
        @wraps(f)
        def wrapper(*args, **kwargs):
            if session.get('logged') == True:
                return f(*args, **kwargs)
            else:
                return jsonify('Unauthorized'), 401
        return wrapper
    
    @staticmethod
    def rate_limit(max_requests=20, window_seconds=60, r=None):
        # Add Rate Limit to the app useing Redis

        if not r:
            r = Connections.C_redis()
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                
                ip = request.remote_addr
                if ip:
                    try:
                        count = r.incr(ip)
                    except:
                        return f(*args, **kwargs)
                    if count == 1:
                        r.pexpire(ip, window_seconds*1000)

                    if count > max_requests:
                        return jsonify({
                            "error": "Too Many Requests",
                            "message": f"Rate limit exceeded. Try again in {window_seconds} seconds."
                        }), 429
                return f(*args, **kwargs)
            return wrapper
        return decorator
    
    @staticmethod
    def admin_required(f):
        # Decorator to check if the user is an admin before allowing access to a route
        @wraps(f)
        def wrapper(*args, **kwargs):
            if session.get('admin') == True:
                return f(*args, **kwargs)
            else:
                return jsonify('Unauthorized'), 401
        return wrapper
