from flask import sessions, session, jsonify
import sqlite3, psycopg2
import json, os
import re


class val:
    password_regex = r"^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$"
    email_regex = r"^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$"
    phone_regex= r"/(?:([+]\d{1,4})[-.\s]?)?(?:[(](\d{1,3})[)][-.\s]?)?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,9})/g"

    def chk_p(password):
        # Checks for password containing at least 1 Upper case, 1 lower case, 1 digit and 1 special character,
        # all together with a length of at least 8. (This pattern allows any order of the requried elements,
        # other than what was been distributed here before)
        __p = re.search(val.password_regex, password)
        if __p:
            return True
    def chk_e(email):
        #Email address compliant with RFC2822
        __e = re.search(val.email_regex, email)
        if __e:
            return True
    def chk_ph(phone):
        #Detects most of the phone numbers all over the world
        __ph = re.search(val.phone_regex, phone)
        if __ph:
            return True

class res:
    def success_response(data):
        pass

    def error_response(message, code):
        pass

class req:
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

class database:
    def sqlite(database):
        conn = sqlite3.connect(database)
        db = conn.cursor()
        return db

    def postgresql(database, user, password, host):
        conn = psycopg2.connect(database=database, user=user, password=password, host=host)
        db = conn.cursor()
        return db


