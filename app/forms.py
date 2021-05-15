from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from app.models import DataRequired

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()],message='Please Enter a Username')
    email=StringField('Email',validators=[DataRequired()],message='Please Enter an Email')
    password=PasswordField('Password',validators=[DataRequired()],message='Please Enter a Password')
    repeatpassword=PasswordField('Repeat Password',validators=[DataRequired()],EqualTo('password'),message='Passwords must match')
    submit=SubmitField('Submit')

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Sign In')
    
