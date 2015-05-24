from flask import render_template, flash, redirect
from app import app, db, models
from .forms import LoginForm # possible future implementation
from opentok import OpenTok
import unicodedata


#source venv/bin/activate
@app.route('/')
@app.route('/index')
def index():
	sid = ''
	sessions = models.Session.query.all()
	for s in sessions:
		if (s.player1 == None or s.player2 == None):
			sid = s.id
	if sid =='':
		opentok = OpenTok('45228402', 'cc334f55939e584275f9c3ba975114c4635953ec')
		session = opentok.create_session()
		sid = session.session_id
		unicodedata.normalize('NFKD', sid).encode('ascii','ignore')
		s = models.Session(id = sid, player1 = None, player2= None)
		db.session.add(s)
		db.session.commit()
	return redirect('/game/' + sid)

@app.route('/game/<sid>', methods=['GET', 'POST'])
def game(sid):
	opentok = OpenTok('45228402', 'cc334f55939e584275f9c3ba975114c4635953ec')
	session_id = unicode(sid)
	token = opentok.generate_token(session_id)
	session = models.Session.query.filter_by(id = sid).first()
	if session.player1 == None:
		session.player1 = token
	else:
		session.player2 = token
	db.session.commit() #db session, don't confuse with tb session
	return render_template('game.html', token = token, sid = session_id)
