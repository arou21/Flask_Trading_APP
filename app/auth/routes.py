from flask import Blueprint, request, redirect, url_for, jsonify
from models import User
from .forms import UserCreationForm, LoginForm
from flask_login import login_user, logout_user, login_required
from flask_cors import cross_origin
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import Flask, jsonify
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
import alpaca_trade_api as tradeapi

trading_client = TradingClient('PKBL4DREIY800L0SL7J4', 'Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw')

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))

# Get our account information.
account = trading_client.get_account()

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

assets = trading_client.get_all_assets(search_params)

# search for AAPL
aapl_asset = trading_client.get_asset('AAPL')

if aapl_asset.tradable:
    print('We can trade AAPL.')

# preparing market order
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

# preparing limit order
limit_order_data = LimitOrderRequest(
                    symbol="BTC/USD",
                    limit_price=17000,
                    notional=4000,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.FOK
                   )

# Limit order
limit_order = trading_client.submit_order(
                order_data=limit_order_data
              )

api = tradeapi.REST()
# Get our position in AAPL.
aapl_position = api.get_position('AAPL')

# Get a list of all of our positions.
portfolio = api.list_positions()

# Print the quantity of shares for each position.
for position in portfolio:
    print("{} shares of {}".format(position.qty, position.symbol))

















# from trade_api import get_account_data
# import alpaca_trade_api as api
# import alpaca_trade_api as tradeapi
# import random
# from flask_sockets import Sockets
# import json
# import websocket
# from geventwebsocket.handler import WebSocketHandler
# from gevent.pywsgi import WSGIServer
# from flask_cors import CORS
# from cors import setup_cors



auth = Blueprint('auth', __name__, template_folder='auth_templates')

# @app.route('/api/get_account_data')
# def get_account():
#     data = get_account_data()
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)







@auth.route('/api/signup', methods=["GET", "POST"])
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


@auth.route('/api/login', methods=["POST"])
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


