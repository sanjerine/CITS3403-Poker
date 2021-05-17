from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='webadmin', template_mode='bootstrap3')

from flask_admin.contrib.sqla import ModelView

from app import routes, models
from app.models import User, Question, Answer, Results, Feedback, Progress

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(Answer, db.session))
admin.add_view(ModelView(Results, db.session))
admin.add_view(ModelView(Feedback, db.session))
admin.add_view(ModelView(Progress, db.session))


