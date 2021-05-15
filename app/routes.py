from flask import Flask, render_template
from app import app,db
from flask_login import (username...etc)
from app.models import (....)
from app.forms import #all the classes of registration whatever
#flask sqlalchemy import maybe
#any forms we wanna import



@app.before_request
# what we want before request . Timeout , validate etc

@app.route('/')
#all the routes that we want to include underneath here
