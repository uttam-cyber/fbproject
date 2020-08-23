from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation', methods=['post'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')


    return "login to successfully"



if __name__=="__main__":
    app.run(debug=True)
