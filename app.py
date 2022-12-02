from flask import Flask, render_template, redirect
from flask import request
from Blockchain import Blockchain
app = Flask(__name__)
DataBase=Blockchain()

@app.route('/auth', methods=['POST', 'GET'])
def do_auth():
    if request.method == 'POST':
        login = request.form["login1"]
        password=request.form["password1"]
        token=DataBase.sign_in(login=login, password=password)
        if token!=None:
            return redirect('home?token='+token)
        else:
            return render_template('auth_error.html')

    else:
        return render_template('auth.html')


@app.route('/reg', methods=['POST', 'GET'])
def do_reg():
    if request.method == 'POST':
        login = request.form["login"]
        password=request.form["password"]
        if login=="":
            return render_template('reg_error3.html')
        if len(password)<5:
            return render_template('reg_error2.html')
        token=DataBase.create_user(login=login, password=password)
        if token!=None:
            return redirect('home?token='+token)
        else:
            return render_template('reg_error1.html')

    return render_template('reg.html')


@app.route('/', methods=["POST", "GET"])
def auth():
    return render_template("auth.html")



@app.route('/home', methods=["POST", "GET"])
def home():
    if request.method=="GET":
        token=request.args.get('token')
        if token!=None:
            return render_template('home.html')
    return render_template("auth.html")


@app.route('/home/mes')
def mes():
    return render_template("mes.html")

if __name__ == "__main__":
    app.run(debug=True)