from packages import login_required
from flask import session

session['name'] = 'mohamed'

@login_required
def login(name):
    name = 'mohamed'
    print(name)
login('ali')

print(val.chk_e("abdo@gmail.com"))