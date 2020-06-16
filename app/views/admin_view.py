from app import app, db
from app.models.users import User
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/admin/dashboard")
def admin_dashboard():
    if current_user.is_authenticated and current_user.admin:
        print(current_user)
        print(current_user.admin)
        return render_template('/admin/templates/dashboard.html')
    #teste de usuários
    elif current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route("/admin/profile")
def admin_profile():
    return "Admin Profile"

@app.route("/admin/error")
def error():
    return render_template('/admin/templates/errorRegister.html')

@app.route("/admin/register", methods=['GET','POST'])
def register():

    if current_user.is_authenticated and current_user.admin:

        if request.method == 'POST':
    
            first_name = request.form['first_name'].capitalize()
            last_name = request.form['last_name'].capitalize()
            email = request.form['email']
            login = request.form['login']
            password = request.form['password']
            # criar um checkbox para informar se o usuário criado é um admin.
            admin = False
            created_at = User.created_at
            updated_at = User.updated_at

            # válida se existe os dados do formulário
            if first_name and last_name and email and login and password:

                exist_login = User.query.filter_by(login=login).first()
                exist_email = User.query.filter_by(email=email).first()

                    # valida se existe login e email
                if not exist_login and not exist_email:

                    user = User(first_name,last_name,email,login,password,admin,created_at,updated_at)
                    db.session.add(user)
                    db.session.commit()

                    # incrementar página de mensagem de usuário criado
                    flash("Usuário criado com sucesso!")
                    return redirect(url_for('register'))
                else:
                    flash("Login/Email já existe")
                    return redirect(url_for('register'))
            else:
                users = User.query.filter().all()
                return render_template('admin/templates/register.html', users = users)
        else:
            users = User.query.filter().all()
            return render_template('admin/templates/register.html', users = users)
    #teste de usuários
    elif current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))








    
