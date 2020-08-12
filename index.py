# -*- coding: utf-8 -*-
import pyrebase
import os
from flask import *
from data import consulta_inicial

app = Flask(__name__)
app.secret_key = os.urandom(24)
config = {

    "apiKey": "AIzaSyCB_XoI-km0-2g38ii0cm0bWuIZwTDwIY0",
    "authDomain": "login-28fc2.firebaseapp.com",
    "databaseURL": "https://login-28fc2.firebaseio.com",
    "projectId": "login-28fc2",
    "storageBucket": "login-28fc2.appspot.com",
    "messagingSenderId": "213736586827",
    "appId": "1:213736586827:web:c16731d8b506e67f3297ce",
    "measurementId": "G-3DVG5040ZN"

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


@app.route('/', methods=['GET', 'POST'])
def inicio():

    unsuccessful = 'E-mail y/o Contrasenia incorrecta'
    if request.method == 'POST':

        email = request.form['name']
        password = request.form['pass']
        session['password'] = password
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            user_id = user['idToken']
            session['usr'] = user_id

            cursor_home = consulta_inicial.select_inicial()
            data_home = cursor_home.fetchall()

            return render_template('home.html',data_home = data_home)
        except:
            return render_template('login.html', us=unsuccessful)

    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    successful = 'Cuenta creada'
    unsuccessful = 'Usuario ya existe'
    if (request.method == 'POST'):
            email = request.form['name']
            password = request.form['pass']
            try:
                auth.create_user_with_email_and_password(email, password)
                return render_template('crear_cuenta.html',s=successful)
            except :
                return render_template('crear_cuenta.html',us=unsuccessful)

    return render_template('crear_cuenta.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if (request.method == 'POST'):
            email = request.form['name']
            auth.send_password_reset_email(email)
            return render_template('login.html')
    return render_template('recordar_cuenta.html')

@app.route("/logout")
def logout():
    #remove the token setting the user to None
    auth.current_user = None
    session.clear()
    return redirect("/");

if(__name__ == "__main__"):
    #app.run(debug = True)
    app.run("0.0.0.0", 5003)
