from flask import Flask
from config import Config
from models import db,User
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from app.routes import auth
# import asynco 
# from alpaca.data import StockDataStream
# from app.api.routes import trade
# from .rest import REST, TimeFrame, TimeFrameUnit 

# app = Flask(__name__)
# app.config.from_object(Config)
app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": ["Content-Type", "Authorization"]}})


db.init_app(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)



# from . import routes
# from . import models
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

async def handle_data(data):
    stock_data.append(data)
    print(data)

# create a stream object with your API keys
# api_key = 'PKBL4DREIY800L0SL7J4'
# secret_key = 'Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw'
# stream = StockDataStream(api_key, secret_key)

# subscribe to real-time data for a specific stock
# symbol = 'AAPL'
# stream.subscribe(symbol, handle_data)

# # initialize an empty list to store incoming stock data
# stock_data = []

# # define a function to run the asyncio loop
# async def run_stream():
#     await stream.connect()

# # start the asyncio loop and run the stream
# loop = asyncio.get_event_loop()
# loop.create_task(run_stream())

# define a route to get the stock data
@app.route('/api/stock_data', methods=['GET'])
def get_stock_data():
    # return the stock data as a JSON object
    return {'data': stock_data}

app.register_blueprint(auth)
# app.register_blueprint(trade)

# @app.route('/api/data')
# @cross_origin()
# def get_data():
#     data = {
#     'title': 'Example News Article',
#     'date': '2023-03-08',
#     'author': 'Jane Doe',
#     'content': 'This is an example news article. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam rutrum nisl in lacus posuere elementum. Etiam auctor ac nibh a luctus. Duis malesuada tincidunt purus, vel vestibulum mi volutpat ut. Fusce consequat ullamcorper mi, id tempor sapien commodo ut. In faucibus, dolor vel sagittis tincidunt, tortor nisl laoreet velit, ac commodo sapien odio eu nunc. Proin nec nulla tincidunt, cursus mauris id, eleifend elit. Vestibulum sit amet est aliquam, interdum ipsum at, congue magna. Donec varius nisl in felis accumsan, ut pulvinar est malesuada. Fusce lobortis semper leo ac lobortis. Integer rhoncus ac quam sit amet aliquam. Donec tristique sapien a ligula aliquet, at dignissim libero facilisis. Donec faucibus risus sit amet lorem commodo, in pellentesque dolor dignissim. Nullam id lorem at arcu vestibulum faucibus.'
# }

# from flask import Flask
# from config import Config
# from models import db, User
# from flask_migrate import Migrate
# from flask_login import LoginManager
# # from flask_cors import CORS
# # from app.auth.routes import auth
# from app.api.routes import trade
# from flask_cors import cross_origin

# app = Flask(__name__)
# app.config.from_object(Config)
# CORS(app)

# db.init_app(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# app.register_blueprint(auth)
# app.register_blueprint(trade)



# @app.route('/api/data')
# @cross_origin()
# def get_data():
#     data = {
#     'title': 'Example News Article',
#     'date': '2023-03-08',
#     'author': 'Jane Doe',
#     'content': 'This is an example news article. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam rutrum nisl in lacus posuere elementum. Etiam auctor ac nibh a luctus. Duis malesuada tincidunt purus, vel vestibulum mi volutpat ut. Fusce consequat ullamcorper mi, id tempor sapien commodo ut. In faucibus, dolor vel sagittis tincidunt, tortor nisl laoreet velit, ac commodo sapien odio eu nunc. Proin nec nulla tincidunt, cursus mauris id, eleifend elit. Vestibulum sit amet est aliquam, interdum ipsum at, congue magna. Donec varius nisl in felis accumsan, ut pulvinar est malesuada. Fusce lobortis semper leo ac lobortis. Integer rhoncus ac quam sit amet aliquam. Donec tristique sapien a ligula aliquet, at dignissim libero facilisis. Donec faucibus risus sit amet lorem commodo, in pellentesque dolor dignissim. Nullam id lorem at arcu vestibulum faucibus.'
# }







