from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin


db = SQLAlchemy()

# create models from out ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    funds = db.Column(db.Integer, nullable=False)
    

    def __init__(self, first_name, last_name, email, password, funds):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.funds = funds

        
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email" : self.email,
            "password": self.password,
            "funds" : self.funds

            
        }


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(100))
    # Add any other relevant fields for the stock table

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    stock_symbol = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    current_value = db.Column(db.Float)
    # Add any other relevant fields for the position table

    def __init__(self, user_id, stock_symbol, quantity, current_value):
        self.user_id = user_id
        self.stock_symbol = stock_symbol
        self.quantity = quantity
        self.current_value = current_value
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    stock_symbol = db.Column(db.String(255))
    order_type = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(255))
    market_order_id = db.Column(db.String(255))
    external_id = db.Column(db.String(50))
    transaction_id = db.Column(db.Integer,db.ForeignKey('transaction.id'))
    # Add any other relevant fields for the order table
    
    def __init__(self,user_id, stock_symbol, order_type, quantity, status, market_order_id, transaction_id):
        self.user_id = user_id
        self.stock_symbol = stock_symbol
        self.order_type = order_type
        self.quantity = quantity
        self.status = status
        self.market_order_id = market_order_id
        self.transaction_id = transaction_id
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "user_id":self.user_id, 
        "stock_symbol":self.stock_symbol, 
        "order_type":self.order_type, 
        "quantity":self.quantity, 
        "status":self.status, 
        "market_order_id":self.market_order_id, 
        "transaction_id":self.transaction_id, 
        }


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    stock_symbol = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    # Add any other relevant fields for the trade table
    
    def __init__(self, user_id, order_id, stock_symbol, quantity, price, timestamp):
        self.user_id = user_id
        self.order_id = order_id
        self.stock_symbol = stock_symbol
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
              "user_id":self.user_id,  
        "order_id":self.order_id,  
        "stock_symbol":self.stock_symbol,  
        "quantity":self.quantity,  
        "price":self.price,  
        "timestamp":self.timestamp,  
        }


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    transaction_type = db.Column(db.String(255))
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime)
    # Add any other relevant fields for the transaction table

    def __init__(self, user_id,transaction_type,amount,date):
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date

    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,

             "user_id":self.user_id ,
        "transaction_type":self.transaction_type ,
        "amount":self.amount ,
        "date":self.date ,
        }
