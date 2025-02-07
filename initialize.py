from flask import Flask,render_template,request,redirect,url_for
from models import db,Professional,Customers

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'

db.init_app(app)

app.app_context().push()
db.create_all() 

db.session.add(Customers(EMAIL='root@root.com',PASSWORD='root_userser',FULLNAME='rooteshwar',ROOTUSER=True))
db.session.commit()