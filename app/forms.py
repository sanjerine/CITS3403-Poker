from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

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
    
    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username has already been taken, please choose another')
            
    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email has already been used, please use another')
    
