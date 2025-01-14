from flask import Flask,render_template,request,redirect,url_for,flash
from models import db,Professional,Customers
from sqlalchemy import select,and_
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'

db.init_app(app) # connection between flask and sqlalchemy

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
        mary = Customers.query.filter(db.and_(Customers.EMAIL==userName,Customers.PASSWORD == passWord)).all()
        # print(query)
        print(len(mary))
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
        city = request.form.get("inputCity")
        state = request.form.get("inputState")
        pincode = request.form.get("inputZip")
        print(email,password,fullName,address,city,state,pincode)
        
        if email != '' and password != '' and fullName != '' and address != '' and state!='' and pincode != None:
            db.session.add(Customers(EMAIL=email,PASSWORD=password,FULLNAME=fullName,ADDRESS=address,CITY=city,STATE=state,PINCODE=pincode))
            db.session.commit()
            db.session.close()
            flash('Record was successfully added')
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


if __name__ == "__main__":
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'
    # sess.init_app(app)
    app.run(debug=True)