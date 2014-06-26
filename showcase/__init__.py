import logging
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.before_first_request
def setup_logging():
	app.logger.addHandler(logging.StreamHandler())
	app.logger.setLevel(logging.ERROR)

import views
