# from flask import Blueprint, render_template


# home_bp = Blueprint('home', __name__)

# @home_bp.route('/')
# def home():
#     return render_template('home.html')

# # views/stream.py
# from flask import Blueprint
# from flask_sockets import Sockets
# import json
# import websocket

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