from app import app, db
from app.models.users import User
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

@app.route("/login", methods=['GET','POST'])
def login():

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = User.query.filter_by(login=login).first()

        if user and user.verify_password(password):
            login_user(user)
            return redirect('index')

        redirect(url_for('login'))

    return render_template('public/templates/login.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/index")
def index():
    return render_template('public/templates/index.html')

@app.route("/ips")
def ip():
    return render_template('public/templates/ips.html')

@app.route("/documents")
def doc():
    return render_template('public/templates/documents.html')

@app.route("/agenda")
def agenda():
    return render_template('public/templates/agenda.html')
