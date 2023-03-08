import datetime
from app import db


class User(db.Model):
    """
    This is the User db schema
    :param UserMixin: enables the storing
    :param db.Model: an inheritance of the database model
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    hash_password = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.now)