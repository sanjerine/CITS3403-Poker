
  
from flask import Flask, session, render_template, url_for, redirect, flash, request
from app import app,db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import (....)
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from datetime import timedelta
#flask sqlalchemy import maybe
#any forms we wanna import



@app.before_request
# what we want before request . Timeout , validate etc
@app.before_request
def before_request():
  session.permanent = True
  app.permanent_session_lifetime = timedelta(minutes = 5)
  session.modified = True

@app.route('/')
#all the routes that we want to include underneath here
@app.route('/index')
def index():
  if not current_user.is_authenticated:
    return render_template('index.html', title = 'Home') 

@app.route('learn')
def learn():
    return render_template('learn.html', title = 'Learn') 

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))
  

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title = 'Quiz') 

@app.route('/feedback')
def feedback():
    return render_template('feedback.html', title = 'Feedback') 

@app.route('/stats')
def stats():
    return render_template('stats.html', title = 'Statistics') 

    
@app.route('/register')
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("You are now a registered!")
    return redirect(url_for('login'))
  return render_template('register.html', title = 'Register', form=form) 


