from flask import sessions
import json
import re


class val:
    password_regex = r"(?P<password>((?=\S*[A-Z])(?=\S*[a-z])(?=\S*\d)(?=\S*[\!\"\§\$\%\&\/\(\)\=\?\+\*\#\'\^\°\,\;\.\:\<\>\ä\ö\ü\Ä\Ö\Ü\ß\?\|\@\~\´\`\\])\S{8,}))"
    email_regex = r"^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$"

    def chk_p(password):
        # Checks for password containing at least 1 Upper case, 1 lower case, 1 digit and 1 special character,
        # all together with a length of at least 8. (This pattern allows any order of the requried elements,
        # other than what was been distributed here before)
        p = re.search(val.password_regex, password)
        if p:
            return True
    def chk_e(email):
        #Email address compliant with RFC2822
        e = re.search(val.email_regex, email)
        if e:
            return True

def success_response(data):
    pass

def error_response(message, code):
    pass

def login_required(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(session)
    return wrapper

def admin_required(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('ali')
    return wrapper