from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Facility

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	name = StringField('Name of Facility', validators=[DataRequired()])
	phone = StringField('Phone Number', validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField(
		'Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		facility = Facility.query.filter_by(username=username.data).first()
		if facility is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		facility = Facility.query.filter_by(email=email.data).first()
		if facility is not None:
			raise ValidationError('Please use a different email address.')

	def validate_phone(self,phone):
		if len(phone.data) < 10:
			raise ValidationError('Invalid phone number')
		#todo: regex validation of a type of phone number


class CapacityForm(FlaskForm):
	current_capacity=IntegerField('Current Capacity', validators=[DataRequired()])
	max_capacity=IntegerField('Max Capacity', validators=[DataRequired()])
	submit = SubmitField('Update')

class EditProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	name = StringField('Name of Facility', validators=[DataRequired()])
	phone = StringField('Phone Number', validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	submit = SubmitField('Save Changes')

	def validate_username(self, username):
		facility = Facility.query.filter_by(username=username.data).all()
		if len(facility)>1:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		facility = Facility.query.filter_by(email=email.data).all()
		if len(facility)>1:
			raise ValidationError('Please use a different email address.')

	def validate_phone(self,phone):
		if len(phone.data) < 10:
			raise ValidationError('Invalid phone number')