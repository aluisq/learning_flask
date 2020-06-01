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

        if not user or not user.verify_password(password):
            return redirect(url_for('login.html'))
        else:
            login_user(user)
            redirect(url_for('public/templates/index.html'))

    return render_template('public/templates/login.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('public/templates/logout.html'))


@app.route("/index")
def index():
    # print(f"Flask ENV is set to: {app.config['ENV']}")
    # print(f"Flask DB is set to: {app.config['SQLALCHEMY_DATABASE_URI']}")
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
