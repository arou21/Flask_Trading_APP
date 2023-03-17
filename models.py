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
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email" : self.email,
            "password": self.password,
            "funds" : self.funds

            
        }
