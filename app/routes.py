from app import db
from flask_login import login_user, logout_user
from app.models import mes, despesa, receita, usuario
from flask import render_template, redirect, url_for, request

def init_app(app):

    @app.route("/", methods=["GET", "POST"])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            pwd = request.form['senha']

            user = usuario.query.filter_by(email=email).first()

            if not user or not user.verify_pwd(pwd):
                return redirect(url_for('cadastrar'))
                
            login_user(user)
            return redirect(url_for('inicio'))

        return render_template("/login.html")
    
    @app.route("/cadastrar", methods=["GET", "POST"])
    def cadastrar():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            pwd = request.form['senha']

            user = usuario(nome, email, pwd)
            db.session.add(user)
            db.session.commit()
            
            return redirect(url_for('home'))

        return render_template("/cadastrar.html")

    
    @app.route("/home")
    def home():
        return render_template("/login.html")
    
    @app.route("/logout")
    def logout():
        return render_template("/login.html")

    @app.route('/inicio')
    def inicio():
        return render_template('/index.html')

    @app.route('/menu')
    def menu():

        meses = mes.query.all()

        return render_template('/menu.html', meses=meses)

    @app.route('/excluir_desp/<int:id_desp>')
    def excluir_desp(id_desp):
        delete=despesa.query.filter_by(id=id_desp).first()
        mes_id=delete.mes_id
        mes_query=mes.query.filter_by(id=mes_id).first()
        nome_mes=mes_query.mes
        db.session.delete(delete)
        db.session.commit()

        return redirect(url_for('overview', nome_mes=nome_mes))
    
    @app.route('/overview/<nome_mes>', methods=['GET', 'POST'])
    def overview(nome_mes):
        #
        mes_objeto = mes.query.filter_by(mes=nome_mes).first_or_404()
        mes_id = mes_objeto.id
        # Despesas
        despesas = despesa.query.filter_by(mes_id=mes_id).all()

        # Receitas
        receitas = receita.query.filter_by(mes_id=mes_id).all()

        # Adicionar despesas
        if request.method == 'POST':
            desp = despesa()
            desp.descricao = request.form['descricao']
            desp.valor = request.form['valor']
            desp.mes_id = request.form['mes']
            db.session.add(desp)
            db.session.commit()

            return redirect(url_for('overview', nome_mes=nome_mes))


        return render_template('/mes_overview.html', nome_mes=nome_mes, despesas=despesas, receitas=receitas, mes_id=mes_id)

##    @app.route('/editar/<int:despesa_id>', methods=['GET', 'POST'])
##    def editar(despesa_id):
##        despesa = despesa.query.filter_by(id=despesa_id).first_or_404()
##        if request.method == 'POST':
##            despesa.descricao = request.form['descricao']
##            despesa.valor = request.form['valor']
##            db.session.commit()
##            return redirect(url_for('index'))  # Redirecionar para a página inicial ou outra página relevante
##        return render_template('editar.html', despesa=despesa)

    @app.route('/relatorio')
    def relatorio():
        return render_template('/relatorios.html')