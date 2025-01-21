from flask import Flask,render_template,request,redirect,url_for,flash
# from models import db,Professional,Customers
# from sqlalchemy import select,and_
import sqlite3
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'

connection = sqlite3.connect('AZHS.db', check_same_thread=False)
cursor = connection.cursor()
# db.init_app(app) # connection between flask and sqlalchemy

################
# To create all the tables defined in the models
# app.app_context().push()
# db.create_all() #create database or update its schema
#####################




@app. route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        userName = request.form.get('email')
        passWord = request.form.get('password')
        As = request.form.get('inputState')
        # if As == 'Customer':
        #     query = select(Customers).where(and_(Customers.EMAIL==userName,Customers.PASSWORD == passWord))
        # else:
        #     query = select(Professional).where(and_(Professional.EMAIL==userName,Professional.PASSWORD == passWord))
        # mary = Customers.query.filter(db.and_(Customers.EMAIL==userName,Customers.PASSWORD == passWord)).all()
        mary = cursor.execute(f"SELECT * FROM Users WHERE EMAIL='{userName}' AND PASSWORD='{passWord}'").fetchall()
        print(type(mary))
        print(mary[0])
        if len(mary)>0 :
            return render_template('successful.html',user=userName,c_p=As)
        return render_template('home.html')
    else:
        return render_template('home.html')

@app.route('/customerSignup', methods=['GET','POST'])
def Csignup():
    if request.method == 'POST' :
        email = request.form.get('inputEmail')
        password = request.form.get("inputPassword")
        fullName = request.form.get("fullName")
        address = request.form.get("inputAddress")
        pincode = request.form.get("inputZip")
        role = 'Customer'
        print(email,password,fullName,address,pincode)
        
        if email != '' and password != '' and fullName != '' and address != '' and pincode != None:
            # db.session.add(Customers(EMAIL=email,PASSWORD=password,FULLNAME=fullName,ADDRESS=address,CITY=city,STATE=state,PINCODE=pincode))
            cursor.execute(f"INSERT INTO Users (EMAIL,PASSWORD,NAME,ADDRESS,ROLE,PIN_CODE) VALUES ('{email}','{password}','{fullName}','{address}','{role}','{pincode}')")
            flash('Record was successfully added')
            connection.commit()
            return """<h1>Registration successful</h1>
                    <a href="/">Click here to Login</a>"""
        return """<a>Please fill all the fields </a>
                    <a href='/customerSignup'>Click here to go back</a>"""
    else:
        return render_template('customerSignup.html')


@app.route('/professionalSignup', methods=['GET','POST'])
def Psignup():
    return render_template('professionalSignup.html')

@app.route('/signin')
def signin():
    return 'Login Success'

# @app.route('/account')
# def account(User,Cp):
#     return render_template('successful.html',user=User,c_p=Cp)
# connection.close()

if __name__ == "__main__":
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'
    # sess.init_app(app)
    app.run(debug=True)