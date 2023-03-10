from app import app, db
from flask import request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return user

@token_auth.verify_token
def verify_token(token):
    user = User.verify_token(token)
    if user:
        return user

@app.route('/api/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        }
        return ('', 204, headers)
    else:
        user = basic_auth.current_user()
        if user:
            return {
                'status': 'ok',
                'user': user.to_dict()
            }
        else:
            return {
                'status': 'not ok'
            }, 400