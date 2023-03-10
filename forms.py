from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchem
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class UserCreationForm(FlaskForm):
    first_name = StringField("first_name", validators=[DataRequired()])
    last_name = StringField("last_name", validators=[DataRequired()])
    username = StringField("user_name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField()
# from flask_wtf import FlaskForm
# from flask_sqlalchemy import SQLAlchemy
# from wtforms import StringField, PasswordField, SubmitField, IntegerField
# from datetime import datetime
# from wtforms.validators import DataRequired, Email, EqualTo

# class UserCreationForm(FlaskForm):
#     first_name = StringField("first_name", validators=[DataRequired()])
#     last_name = StringField("last_name", validators=[DataRequired()])
#     username = StringField("user_name", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField()

# class LoginForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     submit = SubmitField()