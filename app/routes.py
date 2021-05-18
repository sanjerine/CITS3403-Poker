
  
from flask import Flask, session, render_template, url_for, redirect, flash, request
from app import app,db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Question, Answer, Feedback, Results
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from datetime import timedelta
from sqlalchemy import func
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
    return render_template('index.html', title = 'Home') 


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

@app.route('/rules')
@login_required
def rules():
    return render_template('rules.html', title = 'Rules') 

  

@app.route('/quiz', methods = ['GET', 'POST'])
@login_required
def quiz():

    #questions = Question.query.filter_by(question.id = id) #HOW TO JUST GET ALL QUESTION maybe function in data base
    questions = Question.query.all()
    answer=Answer.query.all()
    
    result = 0
                            
    if request.method =="POST":
        
        for question in questions:
            qid = str(question.id)
            qbody = request.form[qid]
            if Answer.query.filter_by(answerbody = qbody).first().answerid:
                result += 1
                            
        if not bool(Results.query.filter_by(userid = current_user.id).first()):
            results = Results(user = current_user)
            db.session.add(results)
            db.session.commit()
        current_user.userresult[0].result = result
        db.session.commit()                   
                            
        return redirect(url_for('index'))                 
                            
    return render_template('quiz.html', title = 'Quiz', questions = questions,answer=answer) 

@app.route('/tutorial', methods = ['GET', 'POST'])
@login_required
def tutorial():

    if request.method=="POST":
        if not bool(TutorialResults.query.filter_by(userid = current_user.id).first()):
            results=Results(userres=current_user)
            db.session.add(results)
            db.session.commit()
        current_user.userresult.result = result
        db.session.commit()

        return redirect(url_for('index'))                 
                            
    return render_template('tutorial.html', title = 'tutorial')
    


@app.route('/feedback', methods = ['GET', 'POST'])
@login_required
def feedback():
    if request.method == "POST":
        feedbackrequest = request.form['feedback']
        if not bool(Feedback.query.filter_by(user_id = current_user.id).first()):
            feedback = Feedback(userfeedback = current_user)
            db.session.add(feedback)
            db.session.commit()
                                   
        current_user.feedback.filter_by(user_id = current_user.id).first().feedbackmsg = feedbackrequest  #note maked feedback data base feedback into feedbackmsg
        db.session.commit()

        return redirect(url_for('index')) 
                      
    cresult = ""
    qsum = 10
    percentage = ""                               
                                   
    if bool(Results.query.filter_by(userid = current_user.id).first()):    #ummm dunno lol
        cresult = int(current_user.userresult[0].result)
        percentage = int((cresult/qsum) *100)                           
                                                                      
    return render_template('feedback.html', title = 'Feedback', result = cresult, sum = qsum, percentage = percentage) 

@app.route('/statistics')
def stats(): 
    #tutorial_results=[]
    #for result in db.session.query(TutorialResults.result).join(User).filter(User.id==(current_user.get_id())):
        #tutorial_results.append(result)
    highscores=[]
    #for score,username in db.session.query(TutorialResults.highscore).join(User).filter((User.id==(current_user.get_id()).orderby(TutorialResults.highscore.amount.desc().limit(10)):
        #highscores.append([username,score])
    numUsers=db.session.query(User).count()


    return render_template('statistics.html', title = 'Statistics')
    
@app.route('/register', methods = ['GET', 'POST'])
def register():

  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("You are now a registered!")
    return redirect(url_for('index'))
  return render_template('register.html', title = 'Register', form=form) 


@app.route('/admin', methods = ['GET', 'POST'])
@login_required
def admin():
    return render_template('admin/index.html', title = 'Admin')            
                                 
                       
