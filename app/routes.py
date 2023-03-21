from flask import Blueprint, request, redirect, url_for, jsonify
from models import User,Transaction,Order,Trade,Position
# from .forms import UserCreationForm, LoginForm
from flask_login import login_user, logout_user, login_required
from flask_cors import cross_origin
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import Flask, jsonify
import requests
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import alpaca_trade_api as tradeapi
import datetime
# from alpaca.data import StockDataStream
# import asyncio
# from alpaca.data import StockDataStream
# api = tradeapi.REST()

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

# stock_stream = StockDataStream("PKBL4DREIY800L0SL7J4", "secret-key")

trading_client = TradingClient('PKBL4DREIY800L0SL7J4', 'Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw', paper=True)

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))


# # Check our current balance vs. our balance at the last market close
# balance_change = float(account.equity) - float(account.last_equity)
# print(f'Today\'s portfolio balance change: ${balance_change}')

# # search for US equities
# search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

# assets = trading_client.get_all_assets(search_params)

# # search for AAPL
# aapl_asset = trading_client.get_asset('AAPL')

# if aapl_asset.tradable:
#     print('We can trade AAPL.')

# # preparing market order
# market_order_data = MarketOrderRequest(
#                     symbol="SPY",
#                     qty=0.023,
#                     side=OrderSide.BUY,
#                     time_in_force=TimeInForce.DAY
#                     )

# Market order
# market_order = trading_client.submit_order(
#                 order_data=market_order_data
#                )

# # preparing limit order
# limit_order_data = LimitOrderRequest(
#                     symbol="BTC/USD",
#                     limit_price=17000,
#                     notional=4000,
#                     side=OrderSide.SELL,
#                     time_in_force=TimeInForce.FOK
#                    )

# # Limit order
# limit_order = trading_client.submit_order(
#                 order_data=limit_order_data
#               )

# api = tradeapi.REST()
# # Get our position in AAPL.
# aapl_position = api.get_position('AAPL')

# # Get a list of all of our positions.
# portfolio = api.list_positions()

# # Print the quantity of shares for each position.
# for position in portfolio:
#     print("{} shares of {}".format(position.qty, position.symbol))


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



@auth.route('/api/news', methods=["GET"])
def get_news():
    url = 'https://data.alpaca.markets/v1beta1/news?exclude_contentless=true'
    headers = {
        'Apca-Api-Key-Id': 'PKBL4DREIY800L0SL7J4',
        'Apca-Api-Secret-Key': 'Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        return jsonify(response_data)
    else:
        return 'Error: ' + str(response.status_code), response.status_code

# def toDictionary(obj):
#     result = {}
#     for key, value in obj:
#         result[key] =value
#     return result

@auth.route('/api/buystock', methods= ["POST"])
@basic_auth.login_required
def buystock():
    user = basic_auth.current_user()
    data=request.json

    # access items from data as data[some_key]

    ## save request to data base
    # buy stock
    ## if successful, then add the order id the reques
    
    ## make transaction and save
    print((request))
    stock_ticker=data['symbol']
    amount=data['quantity']

    transaction = Transaction(user.id, "stock_purchase",amount,datetime.datetime.utcnow() )
    transaction.saveToDB()
    ## make buy stock with transaction_id
    ## save stock purchase

   
  
    # preparing market order
    market_order_data = MarketOrderRequest(
                    symbol=stock_ticker,
                    qty=amount,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

    # Market order
    market_order = trading_client.submit_order(
                order_data=market_order_data
               )
    print(market_order)

    db_order = Order(user.id,market_order.symbol,market_order.type,market_order.qty,market_order.status,market_order.id,transaction.id )

    db_order.saveToDB()

    return jsonify(db_order.to_dict())
    # return jsonify({
    #     'id': db_order.id,
    #     'transaction_id': db_order.transaction_id,
    #     'order_id': market_order.id,
    #     'symbol': market_order.symbol,
    #     'qty': market_order.qty,
    #     'side': market_order.side,
    #     'type': market_order.type,
    #     'status': market_order.status,
    #     'created_at': market_order.created_at,
    #     'submitted_at': market_order.submitted_at,
    # })
               


# Define a helper function to query the database
def get_order(order_id):
    return Order.query.get(order_id)

# Define a Flask route to get all orders
@auth.route('/api/orders', methods= ["GET"])
@basic_auth.login_required
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

# Define a Flask route to get a specific order
@auth.route('/orders/<int:order_id>', methods=['GET'])
@basic_auth.login_required
def get_order_detail(order_id):
    order = get_order(order_id)
    if order:
        return jsonify(order.to_dict())
    else:
        return jsonify({'error': 'Order not found'}), 404


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


# # Define a Flask route to retrieve account information
@auth.route('/account')
@basic_auth.login_required
def get_account_info():
    account_info = trading_client.get_account()
    return jsonify({
        'id': account_info.id ,#:  # The unique identifier for the account.
'account_number': account_info.account_number ,#:  # The account number associated with the account.
'status': account_info.status ,#:  # The current status of the account, either "ACTIVE" or "SUSPENDED".
'currency': account_info.currency ,#:  # The base currency used for the account.
'buying_power': account_info.buying_power ,#:  # The amount of buying power available for the account.
'cash': account_info.cash ,#:  # The amount of cash available for the account.
'portfolio_value': account_info.portfolio_value ,#:  # The total value of all assets in the account, including cash.
'pattern_day_trader': account_info.pattern_day_trader ,#:  # A boolean indicating whether the account is classified as a pattern day trader.
'trading_blocked': account_info.trading_blocked ,#:  # A boolean indicating whether trading is currently blocked for the account.
'transfers_blocked': account_info.transfers_blocked ,#:  # A boolean indicating whether transfers are currently blocked for the account.
'account_blocked': account_info.account_blocked ,#:  # A boolean indicating whether the account is currently blocked for any reason.
'created_at': account_info.created_at ,#:  # The date and time when the account was created.
    })

    

def positionToDict(position):
    
    return {
        "asset_id":position.asset_id,
"symbol":position.symbol,
"exchange":position.exchange,
"asset_class":position.asset_class,
"avg_entry_price":position.avg_entry_price,
"qty":position.qty,
"side":position.side,
"market_value":position.market_value,
"cost_basis":position.cost_basis,
"unrealized_pl":position.unrealized_pl,
"unrealized_plpc":position.unrealized_plpc,
"unrealized_intraday_pl":position.unrealized_intraday_pl,
"unrealized_intraday_plpc":position.unrealized_intraday_plpc,
"current_price":position.current_price,
"lastday_price":position.lastday_price,
"change_today":position.change_today,
    }
    
    
# # Define a Flask route to retrieve account information
@auth.route('/positions')
@basic_auth.login_required
def getPositions():
    position_info = trading_client.get_all_positions()
    positions = [positionToDict(position) for position in position_info]
    return jsonify(positions)
    
# # Define a Flask route to retrieve account information


@auth.route('/sell-position', methods=['GET', 'POST'])
@basic_auth.login_required
def sell_position():
    if request.method == 'POST':
        # process the sell position request
        symbol = request.form.get('symbol')
        qty = request.form.get('qty')
        order = trading_client.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='limit',
            time_in_force='gtc',
            
        )
        return jsonify("position sold")
    else:
        # handle GET requests (if needed)
        return "This endpoint only accepts POST requests for selling positions."


# @auth.route('/sell-position/<symbol>/<qty>')
# @basic_auth.login_required
# def sell_position(symbol, qty):
#     order = trading_client.submit_order(
#         symbol=symbol,
#         qty=qty,
#         side='sell',
#         type='limit',
#         time_in_force='gtc',
#         limit_price=0.01  # replace with your desired limit price
#     )
#     return jsonify("position sold")
