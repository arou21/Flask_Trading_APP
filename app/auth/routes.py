from flask import Blueprint, request, redirect, url_for, jsonify
from models import User
from .forms import UserCreationForm, LoginForm
from flask_login import login_user, logout_user, login_required
from flask_cors import cross_origin
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import Flask, jsonify
# import alpaca_trade_api as api
# import alpaca_trade_api as tradeapi
import random
# from flask_sockets import Sockets
import json
# import websocket
# from geventwebsocket.handler import WebSocketHandler
# from gevent.pywsgi import WSGIServer
# from flask_cors import CORS
# from cors import setup_cors



auth = Blueprint('auth', __name__, template_folder='auth_templates')




# app = Flask(__name__)
# setup_cors(app)

def get_latest_news():
    headers = {
        'Apca-Api-Key-Id': '<PKBL4DREIY800L0SL7J4>',
        'Apca-Api-Secret-Key': '<Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw>'
    }
    url = 'https://data.alpaca.markets/v1beta1/news'
    response = requests.get(url, headers=headers)
    return jsonify(response.json())


@auth.route('/signup', methods=["GET", "POST"])
def signUpPage():
    data=request.json
    print(request.method)
    if request.method == 'POST':
        print(data)
        first_name=data['first_name']
        last_name = data['last_name']
        email = data['email']
        password= data['password'] 
        
        print(first_name, last_name, email, password)

        # add user to database
        user = User(first_name, last_name, email, password,funds=100000)
        print(user)

        user.saveToDB()

            # return redirect(url_for('contactPage'))
        return 'ok'


    return 'hi'
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@auth.route('/login', methods=["POST"])
@basic_auth.login_required
# Login Function
def getToken():
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

@basic_auth.verify_password
def verifyPassword(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return user

@token_auth.verify_token
def verifyToken(token):
    user = User.verify_token(token)
    if user:
        return user






# Initialize the Flask app
# app = Flask(__name__)

# # Configure Alpaca API credentials
# API_KEY = "<PKBL4DREIY800L0SL7J4>"
# API_SECRET = "<Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw>"
# BASE_URL = "https://paper-api.alpaca.markets"
# alpaca = api.REST(API_KEY, API_SECRET, BASE_URL)

# # Define a Flask route to retrieve account information
# @app.route('/account')
# def get_account_info():
#     account_info = trading_client.get_account()
#     return jsonify(account_info)


