from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')
"""
class InstitutionForm(FlaskForm):
	hospital_name = StringField('Name of Hospital', validators=[DataRequired()])
	address_of_hospital = StringField('Address of Hospital', validators=[DataRequired()])
	phone_number = StringField('Phone Number',validators=[DataRequired()])
"""