from app import db
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(30), nullable= False)
    last_name = db.Column(db.String(30), nullable= False)
    email = db.Column(db.String(80), nullable= False, unique=True)
    login = db.Column(db.String(65), nullable= False, unique=True)
    password = db.Column(db.String(200), nullable= False)

    def __init__(self,first_name, last_name, email, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login = login
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"<User: {self.first_name} {self.last_name}>"