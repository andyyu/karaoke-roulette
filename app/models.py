from app import db

class Session(db.Model):
    s_id = db.Column(db.String(256), primary_key=True)
    player1 = db.Column(db.String(256), index=True, unique=True, nullable=True)
    player2 = db.Column(db.String(256), index=True, unique=True, nullable=True)

    def is_full(self):
    	return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User1: %r>, <User2: %r>' % (self.player1, self.player2)