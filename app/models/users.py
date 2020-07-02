from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(30), nullable= False)
    last_name = db.Column(db.String(30), nullable= False)
    email = db.Column(db.String(80), nullable= False, unique=True)
    login = db.Column(db.String(65), nullable= False, unique=True)
    password = db.Column(db.String(200), nullable= False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


    def __init__(self,first_name, last_name, email, login, password,admin,created_at,updated_at):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login = login
        self.password = generate_password_hash(password)
        self.admin = admin
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def verify_password(self,password_form):
        return check_password_hash(self.password, password_form)

    def __repr__(self):
        return f"<User: {self.first_name} {self.last_name}>"