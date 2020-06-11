from app import app
import jwt

class Auth:
    def create(payload):
        create_token = jwt.encode(payload,app.config['SECRET_KEY'], algorithm='HS256')

        return create_token

    def checked(token):
        checked_token = jwt.decode(token,app.config['SECRET_KEY'],algorithm='HS256').get("login")
        return checked_token