from packages import req, database, val
from flask import Flask, session, request
import json

app = Flask(__name__)
app.secret_key = '1234567890'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    session['logged'] = True
    return 'Logged in'

@app.route('/test')
@login_required
def test():
    name = 'mohamed'
    print(name)
    return name

@app.route('/login_admin')
def login_admin():
    session['admin'] = True
    return 'Admin logged in'

@app.route('/admin')
@admin_required
def admin():
    return 'admin'

@app.route('/logout')
def logout():
    session.pop('logged', None)
    session.pop('admin', None)
    return 'Logged out'


if __name__ == '__main__':
    app.run(debug=True)
