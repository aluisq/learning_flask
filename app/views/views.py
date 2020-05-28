from app import app
from flask import render_template


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/index")
def index():
    print(f"Flask ENV is set to: {app.config['ENV']}")
    print(f"Flask DB is set to: {app.config['SQLALCHEMY_DATABASE_URI']}")
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
