from app import db

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

