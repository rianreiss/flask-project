from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/relatorio')
def relatorio():
    return render_template('relatorios.html')