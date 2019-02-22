from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	#location
	#position
	password_hash = db.Column(db.String(128))
	#backrefhospital?

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Facility(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	#address
	#phone
	#max_capacity
	#current_capacity

	def __repr__(self):
		return '<Facility {}>'.format(self.name) 