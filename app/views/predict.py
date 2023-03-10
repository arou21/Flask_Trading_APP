# from flask import Flask, jsonify, request
# import numpy as np
# import joblib

# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the request payload as a dictionary
#     data = request.get_json()

#     # Convert the dictionary to a numpy array
#     features = np.array([list(data.values())])

#     # Load the trained model from disk
#     model = joblib.load('model.pkl')

#     # Use the model to make predictions
#     prediction = model.predict(features)

#     # Return the predictions as a JSON response
#     return jsonify({'prediction': prediction[0]})

# def predict(data):
#     # Convert the dictionary to a numpy array
#     features = np.array([list(data.values())])

#     # Load the trained model from disk
#     model = joblib.load('model.pkl')

#     # Use the model to make predictions
#     prediction = model.predict(features)

#     return prediction[0]

# @app.route('/make_prediction', methods=['POST'])
# def make_prediction():
#     data = request.get_json()
#     prediction = predict(data)
#     response = {'prediction': prediction}
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, Blueprint, request, jsonify
# from flask_sockets import Sockets
# import json
# import websocket


# # Create the stream Blueprint
# stream_bp = Blueprint('stream', __name__)
# sockets = Sockets(stream_bp)

# @sockets.route('/stream')
# def stream(ws):
#     # Connect to the Alpaca news stream endpoint
#     ws = websocket.WebSocketApp("wss://stream.data.alpaca.markets/v1beta1/news",
#                                 on_message=on_message,
#                                 on_error=on_error,
#                                 on_close=on_close)

#     # Start the WebSocket client
#     ws.run_forever()

# def on_message(ws, message):
#     # Broadcast the incoming message to all connected WebSocket clients
#     sockets.broadcast(json.dumps(message))

# def on_error(ws, error):
#     print(error)

# def on_close(ws):
#     print("### closed ###")

# # Create the Flask app and register the stream Blueprint
# app = Flask(__name__)
# app.register_blueprint(stream_bp)

# if __name__ == '__main__':
#     app.run(debug=True)






# from flask import Blueprint, request, redirect, url_for, jsonify
# import requests

# # trade = Blueprint('trade', __name__,url_prefix="/trade")
# # app = Flask(__name__)

# app = Blueprint('app', __name__, url_prefix="/app")

# from alpaca.trading.client import TradingClient

# # paper=True enables paper trading
# api_key_id = 'PKBL4DREIY800L0SL7J4'
# api_secret_key = 'Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw'

# # Replace this value with the Alpaca API server you want to use
# api_server = 'https://api.alpaca.markets'

# # Set up the API request headers with the API key and secret key
# headers = {
#     'APCA-API-KEY-ID': api_key_id,
#     'APCA-API-SECRET-KEY': api_secret_key,
# }

# # Make the API request to retrieve account information
# response = requests.get(f'{api_server}/v2/account', headers=headers)

# # Check if the API call was successful (HTTP status code 200)
# if response.status_code == 200:
#     # Print the account information in JSON format
#     print(response.json())
# else:
#     # Print the error message if the API call was unsuccessful
#     print(f'Error: {response.json()["message"]}')
# trading_client = TradingClient(paper=True)

# @app.route('/AAPL/chartdata')
# def get_chart_data():
#     url = 'https://api.polygon.io/v1/marketstatus/now?apiKey=RrDmtncR5mw_qpwqwSJJrzJHycXc0XoT'
#     res = requests.get(url)
#     data = res.json()
#     print(data)
#     return jsonify(data)


