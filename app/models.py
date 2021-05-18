#database
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import random



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    feedback = db.relationship('Feedback', backref='userfeedback', lazy ='dynamic')
    userresult = db.relationship('Results', backref='user', lazy = 'dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Feedback (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedbackmsg = db.Column(db.Text, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Question (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    questionbody = db.Column(db.Text, index=True)
    mark = db.Column(db.Integer, index = True, default = "1")
    answers = db.relationship('Answer', backref= 'question', lazy = True)
    
    def __repr__(self):
        return 'Question {}: '.format(self.id) + '{}'.format(self.questionbody)
    
    def get_question(self):
        questions = []
        for question in Question.questionbody:
            questions.append(question)
            
    
    def get_randomised_answers(self):
        answers = Answer.query.filter_by(questionid = self.id).all()
        random.shuffle(answers)
        return answers
    
    def get_correct_answer(self):
        return Answer.query.filter_by(questionid = self.id, answerid = 1).first()
    
    
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answerbody = db.Column(db.Text, index=True)
    questionid = db.Column(db.Integer, db.ForeignKey('question.id'))
    answerid = db.Column(db.Boolean, default= False, nullable = False)
    
    def __repr__(self):
        return 'Answer: {}: '.format(self.option_body)
    
    def check_correct(self):
        return self.answerid 
    
class Results(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    result = db.Column(db.Integer)
    highscore = db.Column(db.Integer)
    
class TutorialResults(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    result = db.Column(db.Integer)


class Progress(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    progress = db.Column(db.Integer)
#create database using mixin from flask_login or otherwise
#one for users, one for the poker hands (4 suits, 13 cards), one for outcome? dunno
