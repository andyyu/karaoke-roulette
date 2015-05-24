from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config.from_object('config')
db = SQLAlchemy(app)

class TbSession(db.Model):
    id = db.Column(db.String(256), primary_key=True)
    player1 = db.Column(db.String(256), index=True, unique=True, nullable=True)
    player2 = db.Column(db.String(256), index=True, unique=True, nullable=True)

    def is_full(self):
    	return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)

    def __init__(self, player1, player2):
    	self.player1 = player1
    	self.player2 = player2

    def __repr__(self):
        return '<User1: %r>, <User2: %r>' % (self.player1, self.player2)

from app import views, models
