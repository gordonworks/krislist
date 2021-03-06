from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, CapacityForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Facility
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
	facilities = Facility.query.order_by((Facility.max_capacity - Facility.current_capacity).desc()).all()
	return render_template('index.html', title='Home',facilities=facilities)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		facility = Facility.query.filter_by(username=form.username.data).first()
		if facility is None or not facility.check_password(form.password.data):
			flash('Invalid Username/Password')
			return redirect(url_for('login'))
		login_user(facility, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		facility = Facility(username=form.username.data, email=form.email.data,
			name=form.name.data, phone=form.phone.data, address=form.address.data)
		facility.set_password(form.password.data)
		db.session.add(facility)
		db.session.commit()
		flash('Congratulations, you are now a registered facility!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/facility/<int:id>',methods=['GET','POST'])
def facility(id):
	facility = Facility.query.filter_by(id=id).first_or_404()
	form = CapacityForm()
	if form.validate_on_submit() and request.method == 'POST':
		facility.current_capacity = form.current_capacity.data
		facility.max_capacity = form.max_capacity.data
		facility.last_updated = datetime.utcnow()
		db.session.commit()
	return render_template('facility.html', title='View Facility',
	 facility=facility, form=form)

@login_required
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/edit/<int:id>/',methods=['GET','POST'])
@login_required
def edit(id):
	facility =  Facility.query.filter_by(id=id).first_or_404()
	form = EditProfileForm()
	
	if 'save' in request.form:
		print("save button hit")
	
	
	#cancel button vs save button
	if form.validate_on_submit():
		if 'cancel_button' in request.form:
			print('edit canceled')
		else:
			facility.username=form.username.data
			facility.email=form.email.data
			facility.name=form.name.data
			facility.phone=form.phone.data
			facility.address=form.address.data
			db.session.commit()
		#ensures editing a transaction preserves the current page
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
				next_page = url_for('facility',id=current_user.id)
		return redirect(next_page)
	
	return render_template('edit.html',form=form,title="Edit", facility=facility)