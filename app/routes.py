
  
from flask import Flask, render_template
from app import app,db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import (....)
from app.forms import #all the classes of registration whatever
from werkzeug.urls import url_parse
#flask sqlalchemy import maybe
#any forms we wanna import



@app.before_request
# what we want before request . Timeout , validate etc

@app.route('/')
#all the routes that we want to include underneath here
@app.route('/index')
def home():
    return render_template('index.html', title = 'Home') 

@app.route('learn')
def learn():
    return render_template('learn.html', title = 'Learn') 

@app.route('/login')
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

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title = 'Quiz') 

@app.route('/feedback')
def feedback():
    return render_template('feedback.html', title = 'Feedback') 

@app.route('/stats')
def stats():
    return render_template('stats.html', title = 'Statistics') 

@app.route('/logout')
def logout():
    return redirect(url_for('index'))
    
@app.route('/register')
def register():
    return render_template('register.html', title = 'register') 


