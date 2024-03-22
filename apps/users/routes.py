from flask import render_template, redirect, url_for, flash, request, make_response, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from apps import app
from apps.users.model import *
from apps.users.forms import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile', username=current_user.username))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and password == user.password:
            login_user(user)
            return redirect(url_for('index', username=current_user.username))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('login', username=current_user.username))

    form = SignUpForm()  

    if form.validate_on_submit():
        username = form.username.data
        fullname = form.fullname.data 
        email    = form.email.data
        password = form.password.data



        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different username.', 'error')
        else:

            user = User(username=username, fullname=fullname,email=email, password=password)

            db.session.add(user)
            db.session.commit()

            login_user(user)

            return redirect(url_for('login', username=current_user.username))

    return render_template('signup.html', title="Signup", form=form)


