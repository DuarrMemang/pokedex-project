from flask_login import UserMixin

from app import db
from apps import db
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__   = "users"
    id              = db.Column(db.Integer, primary_key = True)
    username        = db.Column(db.String(128), nullable = False)
    password        = db.Column(db.String(128), nullable = False)
    fullname        = db.Column(db.String(128), nullable = False)
    email           = db.Column(db.String(128), nullable = False)