from flask import Flask, redirect, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
#from .forms import LoginForm possible future implementation
from opentok import OpenTok
import os
import unicodedata

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

api_key = ""        # Replace with your OpenTok API key.
api_secret = ""     # Replace with your OpenTok API secret.

class Session(db.Model):
    s_id = db.Column(db.String(512), primary_key=True)
    player1 = db.Column(db.String(512), index=True, unique=True, nullable=True)
    player2 = db.Column(db.String(512), index=True, unique=True, nullable=True)

    def is_full(self):
    	return False

    def get_id(self):
        try:
            return unicode(self.s_id)  # python 2
        except NameError:
            return str(self.s_id)

    def __init__(self, s_id, player1, player2):
        self.s_id = s_id
    	self.player1 = player1
    	self.player2 = player2

    def __repr__(self):
        return '<User1: %r>, <User2: %r>' % (self.player1, self.player2)

@app.route('/')
@app.route('/index')
def index():
    sid = ''
    sessions = Session.query.all()
    for s in sessions:
        if (s.player1 == None or s.player2 == None):
            sid = s.s_id
    if sid =='':
        opentok = OpenTok(api_key, api_secret)
        session = opentok.create_session()
        sid = session.session_id
        unicodedata.normalize('NFKD', sid).encode('ascii','ignore')
        s = Session(s_id = sid, player1 = None, player2= None)
        db.session.add(s)
        db.session.commit()
    return redirect('/game/' + sid)

@app.route('/game/<sid>', methods=['GET', 'POST'])
def game(sid):
    opentok = OpenTok(api_key, api_secret)
    session_id = unicode(sid)
    token = opentok.generate_token(session_id)
    session = Session.query.filter_by(s_id = sid).first()
    if session.player1 == None:
        session.player1 = token
    else:
        session.player2 = token
    db.session.commit() #db session, don't confuse with tb session
    return render_template('game.html', token = token, sid = session_id)

