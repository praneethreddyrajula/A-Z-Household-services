from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

userName = ""
passWord = ""

@app. route('/', methods=['GET','POST'])
def home():
    global userName,passWord
    if request.method == 'POST':
        userName = request.form.get('InputEmail')
        passWord = request.form.get('inputPassword6')
        return render_template('home.html', username=userName,password=passWord )
    
    return render_template('home.html')

@app.route('/customerSignup', methods=['GET'])
def Csignup():
    return render_template('customerSignup.html')

@app.route('/professionalSignup', methods=['GET'])
def Psignup():
    return render_template('professionalSignup.html')

@app.route('/signin')
def signin():
    return 'Login Success'

app.run(debug=True)