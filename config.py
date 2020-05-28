

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "@rrozdoce"
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    UPLOADS = "/home/username/app/app/static/img/uploads"
    SESSION_COOKIE_SECURE = True
    BOOTSTRAP_SERVE_LOCAL = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    UPLOADS = "/home/username/learning_flask/app/app/static/img/uploads"
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bigbox.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    UPLOADS = "/home/username/learning_flask/app/app/static/img/uploads"
    SESSION_COOKIE_SECURE = False
