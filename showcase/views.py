from flask import render_template, url_for, redirect, flash, jsonify, request
from flask.ext.login import login_user, logout_user, current_user, login_required

from . import app, db
from .models import *
from .forms import *

@app.route('/')
def home_page():
	return render_template('home.html', user=current_user)

@app.route('/tickets')
def tickets_page():
	return render_template('tickets.html')

@app.route('/performers')
#@login_required
def performers_page():
	return render_template('performers.html')

@app.route('/dvds')
def dvds_page():
	return render_template('dvds.html')

@app.route('/program')
def program_page():
	return render_template('program.html')



#
#  Account Functions
#

@app.route('/accounts/login', methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.is_correct_password(form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('home_page'))
        else:
            flash("Sorry, your information doesn't seem right", "warning")
            return redirect(url_for('login'))

    return render_template("accounts/login_page.html", form=form)


@app.route('/accounts/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))


@app.route('/accounts/create', methods=["GET", "POST"])
def create_account():
    form = UniqueEmailNamePasswordForm()

    if form.validate_on_submit():
        print "Creating Account..."
        user = User(
            email = form.email.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()

        login_user(user, remember=True)

        flash("Account created! Welcome " + user.first_name + "!", "success")
        return redirect(url_for('home_page'))

    return render_template('accounts/create_page.html', form=form)