from app import db
from app.models import mes, despesa, receita
from flask import render_template, redirect, url_for

def init_app(app):

    @app.route('/')
    def index():
        return render_template('/index.html')

    @app.route('/menu')
    def menu():

        meses = mes.query.all()

        return render_template('/menu.html', meses=meses)
    
    @app.route('/overview/<string:nome_mes>', methods=['GET', 'POST'])
    def overview(nome_mes):
        #
        mes_objeto = mes.query.filter_by(mes=nome_mes).first_or_404()
        mes_id = mes_objeto.id
        # Despesas
        despesas = despesa.query.filter_by(mes_id=mes_id).all()

        # Receitas
        receitas = receita.query.filter_by(mes_id=mes_id).all()


        return render_template('/mes_overview.html', nome_mes=nome_mes, despesas=despesas, receitas=receitas)

    @app.route('/relatorio')
    def relatorio():
        return render_template('/relatorios.html')