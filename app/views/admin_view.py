from app import app, db
from app.models.users import User
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template('/admin/templates/dashboard.html')

@app.route("/admin/profile")
def admin_profile():
    return "Admin Profile"

@app.route("/admin/error")
def error():
    return render_template('/admin/templates/errorRegister.html')

@app.route("/admin/register", methods=['GET','POST'])
def register():

    if request.method == 'POST':

        first_name = request.form['first_name'].capitalize()
        last_name = request.form['last_name'].capitalize()
        email = request.form['email']
        login = request.form['login']
        password = request.form['password']
        admin = False
        created_at = User.created_at
        updated_at = User.updated_at

        # válida se existe os dados do formulário
        if first_name and last_name and email and login and password:

            # valida se existe login e email
            exist_login = User.query.filter_by(login=login).first()
            exist_email = User.query.filter_by(email=email).first()

            if not exist_login and not exist_email:
                user = User(first_name,last_name,email,login,password,admin,created_at,updated_at)
                db.session.add(user)
                db.session.commit()
                # incrementar página de mensagem de usuário criado
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('error'))
        else:
            users = User.query.filter().all()
            return render_template('admin/templates/register.html', users = users)
    else:
        return render_template('admin/templates/register.html')
