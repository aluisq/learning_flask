from app import app, db
from app.models.users import User
from flask import render_template, request, redirect, url_for, send_file
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/login", methods=['GET','POST'])
def login():

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        
        user = User.query.filter_by(login=login).first()

        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('index'))

        else:
            error = "Login/Password inválido"
            return render_template('public/templates/login.html', error = error)

    else:
        return render_template('public/templates/login.html')
    
    
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/")
def index():
    return render_template('public/templates/index.html')

@app.route("/ips")
def ips():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        users = User.query.filter().all()
        return render_template('public/templates/ips.html', users = users )

@app.route("/documents")
def doc():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return render_template('public/templates/documents.html')

@app.route('/documents/teste')
def doc_pdf():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return send_file('static/pdf/teste.pdf')

@app.route("/agenda")
def agenda():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return render_template('public/templates/agenda.html')
