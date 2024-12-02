# Orm
# Schema of the db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Professional(db.Model):
    ID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    EMAIL = db.Column(db.String(255),unique=True, nullable=False)
    PASSWORD = db.Column(db.Text,nullable=False)
    FULLNAME = db.Column(db.String(255), nullable=False)
    SERVICENAME = db.Column(db.String(255))
    EXPERIENCE = db.Column(db.Integer)
    ADDRESS = db.Column(db.Text)
    OINCODE = db.Column(db.Integer)
    ROOTUSER = db.Column(db.Boolean, default=False)

class Customers(db.Model):
    ID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    EMAIL = db.Column(db.String(255),unique=True, nullable=False)
    PASSWORD = db.Column(db.Text,nullable=False)
    FULLNAME = db.Column(db.String(255), nullable=False)
    ADDRESS = db.Column(db.String(255))
    CITY = db.Column(db.String(255))
    STATE = db.Column(db.String(255))
    PINCODE = db.Column(db.Integer)
    ROOTUSER = db.Column(db.Boolean, default=False)
