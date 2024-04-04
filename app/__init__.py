from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuração do aplicativo
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:amsterda01@localhost/finance-app'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'secret'
    app.config['JWT_SECRET_KEY'] = 'secret'
    app.config['JWT_BLACKLIST_ENABLE'] = True
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  # Token sem expiração

    db.init_app(app)

    from app import routes

    return app