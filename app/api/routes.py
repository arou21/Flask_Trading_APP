from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
import alpaca_trade_api as tradeapi

trading_client = TradingClient('api-key', 'secret-key')

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





# from flask import Blueprint, request, redirect, url_for, jsonify
# import requests

# trade = Blueprint('trade', __name__,url_prefix="/trade")




# trade = Blueprint('trade', __name__, url_prefix= "/trade")

# @trade.route('/api/polygon/<ticker>/<date>')
# def get_polygon_data(ticker, date):
#     api_key = "RrDmtncR5mw_qpwqwSJJrzJHycXc0XoT"
#     endpoint = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{date}/{date}"
#     params = {
#         "apiKey": api_key
#     }

#     response = requests.get(endpoint, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         return jsonify(data)
#     else:
#         return "Error: Unable to retrieve data from Polygon API."


# @trade.route('/chartdata', methods=["GET"])
# def chartdata():
    
#     url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=RrDmtncR5mw_qpwqwSJJrzJHycXc0XoT"

#     url = "https://bb-finance.p.rapidapi.com/market/get-chart"

#     querystring = {"id":"inmex:ind","interval":"y1"}

#     headers = {
#         "X-RapidAPI-Key": "ef0eeefccdmshc08de5a0c42a9e2p14d438jsne0c985eb3133",
#         "X-RapidAPI-Host": "bb-finance.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     print(response.text)
#     return response.text
          
 