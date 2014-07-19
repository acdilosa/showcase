import logging
from flask import Flask, g
from flask_bootstrap import Bootstrap
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.before_first_request
def setup_logging():
	app.logger.addHandler(logging.StreamHandler())
	app.logger.setLevel(logging.ERROR)

# Initialize Flask Extensions
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

# Setup User Accounts and Login Management
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message_category = "warning"
login_manager.login_message = u"You need to login to get to that page."

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id == userid).first()

@app.before_request
def before_request():
    g.user = current_user

# Import all the main views
import views