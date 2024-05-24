from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuração do aplicativo
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:amsterda01@localhost/finance-app'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'secret'
    app.config['JWT_SECRET_KEY'] = 'secret'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  # Token sem expiração

    db.init_app(app)
    login_manager.init_app(app)  # Inicializar sem redeclarar

    from app.routes import init_app
    init_app(app)

    return app
