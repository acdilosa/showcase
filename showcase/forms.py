from flask_wtf import Form
from wtforms import TextField, PasswordField, DecimalField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Email
from flask.ext.login import current_user


from .util.validators import Unique
from .models import User


class UniqueEmailNamePasswordForm(Form):
	email = TextField('Email', validators=[DataRequired(), Email(),
		Unique(
			User,
			User.email,
			message="There is already an account with that email."
		)])
	first_name = TextField('First Name', validators=[DataRequired()])
	last_name = TextField('Last Name', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Create Account')

class EmailPasswordForm(Form):
	email = TextField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')