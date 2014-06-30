from flask import render_template
from . import app

@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/tickets')
def tickets_page():
	return "Not Implemented"

@app.route('/performers')
def performers_page():
	return "Not Implemented"

@app.route('/dvds')
def dvds_page():
	return render_template('dvds.html')

@app.route('/program')
def program_page():
	return "Not Implemented"
