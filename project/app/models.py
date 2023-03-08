from datetime import datetime
from app import db, app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """
    This is the User db schema
    :param UserMixin: enables the storing
    :param db.Model: an inheritance of the database model
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.now)
    
    # constructor
    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    # verify password function
    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User : {self.email}'
