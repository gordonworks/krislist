from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
	return Facility.query.get(int(id))

class Facility(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	phone = db.Column(db.String(16), unique=True)
	name = db.Column(db.String(64))
	address = db.Column(db.String(120), index=True, unique=True)
	current_capacity = db.Column(db.Integer)
	max_capacity = db.Column(db.Integer)
	last_updated = db.Column(db.DateTime, default=datetime.utcnow)
	password_hash = db.Column(db.String(128))

	def set_password(self,password):
		self.password_hash = generate_password_hash(password)

	def check_password(self,password):
		return check_password_hash(self.password_hash,password)

	def __repr__(self):
		return '<Facility {}>'.format(self.username)