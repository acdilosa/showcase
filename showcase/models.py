from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import synonym
from flask.ext.login import UserMixin, current_user
from datetime import datetime

from . import bcrypt, db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    _password = db.Column(db.String(128))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    @hybrid_property
    def name(self):
        return self.first_name + " " + self.last_name
    
    def is_correct_password(self, plaintext):
        if bcrypt.check_password_hash(self._password, plaintext):
            return True
        return False

    def __repr__(self):
        return '<User "{id}: {email}">'.format(id=self.id, email=unicode(self.email).encode('ascii', 'ignore'))
