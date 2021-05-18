import os
import unittest

from config import basedir
from app import app, db
from sqlalchemy import func
from app.models import User, Question, Answer, Result

class Test(unittest.TestCase):
    def setUp(self):
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://']
      db.creat_all()
      
    def tearDown(self):
      db.session.remove()
      db.drop_all
      
if __name__ == '__main__':
  unnittest.main()
