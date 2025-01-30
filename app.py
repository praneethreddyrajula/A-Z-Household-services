from flask import Flask,render_template,request,redirect,url_for,flash
# from models import db,Professional,Customers
# from sqlalchemy import select,and_
import sqlite3
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'

connection = sqlite3.connect('AZHS.db', check_same_thread=False)

# db.init_app(app) # connection between flask and sqlalchemy

################
# To create all the tables defined in the models
# app.app_context().push()
# db.create_all() #create database or update its schema
#####################

with sqlite3.connect('AZHS.db', check_same_thread=False) as conn:
    cursor = conn.cursor()
    @app. route('/', methods=['GET','POST'])
    def home():
        if request.method == 'POST':
            userName = request.form.get('email')
            passWord = request.form.get('password')
            userDetails = cursor.execute(f"SELECT * FROM Users WHERE EMAIL='{userName}' AND PASSWORD='{passWord}'").fetchall()
            print(type(userDetails))
            print(userDetails[0])
            if userDetails is not None and userDetails[0][5] == 'Customer' or userDetails[0][5] == 'Professional':
                return render_template('successful.html',user=userName,c_p=userDetails[0][3])
            return render_template('home.html')
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
                cursor.execute(f"""INSERT INTO Users (EMAIL,PASSWORD,NAME,ADDRESS,ROLE,PIN_CODE) VALUES (?,?,?,?,?,?)""",(email,password,fullName,address,role,pincode))
                flash('Record was successfully added')
                conn.commit()
                return """<h1>Registration successful</h1>
                        <a href="/">Click here to Login</a>"""
            return """<a>Please fill all the fields </a>
                        <a href='/customerSignup'>Click here to go back</a>"""
        return render_template('customerSignup.html')


    @app.route('/professionalSignup', methods=['GET', 'POST'])
    def Psignup():
        if request.method == 'POST':
            email = request.form.get('inputEmail')
            password = request.form.get("inputPassword")
            fullName = request.form.get("fullName")
            address = request.form.get("inputAddress")
            pincode = request.form.get("inputZip")
            info_doc = request.files['infoDoc']  # This is the uploaded file
            
            # Read the binary content of the uploaded file
            docData = info_doc.read()
            role = 'Professional'
            
            print(email, password, fullName, address, pincode)
            
            if email != '' and password != '' and fullName != '' and address != '' and pincode != None:
                # Use parameterized queries to avoid SQL injection and issues
                cursor.execute("""
                    INSERT INTO Users (EMAIL, PASSWORD, NAME, ADDRESS, ROLE, PIN_CODE, INFO_DOC)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (email, password, fullName, address, role, pincode, docData))
                
                flash('Record was successfully added')
                conn.commit()
                
                return """<h1>Registration successful</h1>
                        <a href="/">Click here to Login</a>"""
            
            return """<a>Please fill all the fields </a>
                    <a href='/professionalSignup'>Click here to go back</a>"""
    
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