from flask import Flask,render_template,request,redirect,url_for,flash
from models import db,Professional,Customers
from sqlalchemy import select,and_
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'

db.init_app(app)


mary = Customers.query.filter().all()