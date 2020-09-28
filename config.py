from datetime import timedelta

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "@rrozdoce"
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = ""
    UPLOADS = "../../static/img/uploads"
    SESSION_COOKIE_SECURE = True
    BOOTSTRAP_SERVE_LOCAL = True
    PERMANENT_SESSION_LIFETIME =  timedelta(minutes=60)

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "rocketi"
    DB_USERNAME = "root"
    DB_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bigbox.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADS = "../../static/img/uploads"
    SESSION_COOKIE_SECURE = False
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USE_SSL= True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'seuemail'
    MAIL_PASSWORD = 'suasenha'
    MAIL_DEFAULT_SENDER = 'emailpadrao'

class TestingConfig(Config):
    TESTING = True
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    UPLOADS = "/home/username/learning_flask/app/app/static/img/uploads"
    SESSION_COOKIE_SECURE = False
