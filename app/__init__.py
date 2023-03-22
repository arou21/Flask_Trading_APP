from flask import Flask
from config import Config
from models import db,User
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from app.routes import auth
# from app.watchlist import watchlist_bp
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

# define a route to get the stock data
@app.route('/api/stock_data', methods=['GET'])
def get_stock_data():
    # return the stock data as a JSON object
    return {'data': stock_data}

app.register_blueprint(auth)
# app.register_blueprint(watchlist_bp)







