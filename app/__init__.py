from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)

# pega as configurações

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

# instancias para registrar o uso das lib's na aplicação

login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from app.views import user_view, admin_view
from app.models import users, machines

db.init_app(app)
db.create_all()
