#database
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id
    
 
class Feedback (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.Text, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class 

#create database using mixin from flask_login or otherwise
#one for users, one for the poker hands (4 suits, 13 cards), one for outcome? dunno
