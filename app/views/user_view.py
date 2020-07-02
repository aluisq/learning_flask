import datetime
from app import app, db
from app.models.users import User
from app.models.machines import Machine
from flask import render_template, request, redirect, url_for, send_file, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from app.helpers.authentication import Auth

@app.route("/login", methods=['GET','POST'])
def login():

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        
        user = User.query.filter_by(login=login).first()

        if not (user and user.verify_password(password)):
            flash('Login/Password inválido')
            return render_template('public/templates/login.html')
        else:
            payload = {
                    "id" : user.id,
                    "login" : user.login,
                    "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
                    }
            token = Auth.create(payload)
            print(token)
            print(Auth.checked(token))
            if user.admin is True:
                login_user(user)
                session.permanent = True
                return redirect(url_for('admin_dashboard'))
            else:
                login_user(user)
                session.permanent = True
                return redirect(url_for('index'))
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
        machines = Machine.query.filter().all()
        return render_template('public/templates/ips.html', machines = machines )

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

# @app.route("/send_email")
# def send_email():