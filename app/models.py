from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return usuario.query.filter_by(id=user_id)

class usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    pwd = db.Column(db.String(256), nullable=False)

    def __init__(self, nome, email, pwd):
        self.nome = nome
        self.email = email
        self.pwd = generate_password_hash(pwd)

    def verify_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


class mes(db.Model):
    __tablename__ = "meses"
    id = db.Column(db.Integer, primary_key=True)
    mes = db.Column(db.String(20), nullable=False)
    total_despesas = db.Column(db.Numeric(10, 2))
    total_receitas = db.Column(db.Numeric(10, 2))
    saldo = db.Column(db.Numeric(10, 2))

class despesa(db.Model):
    __tablename__ = "despesas"
    id = db.Column(db.Integer, primary_key=True)
    mes_id = db.Column(db.Integer, db.ForeignKey('meses.id'), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)

class receita(db.Model):
    __tablename__ = "receitas"
    id = db.Column(db.Integer, primary_key=True)    
    mes_id = db.Column(db.Integer, db.ForeignKey('meses.id'), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)

