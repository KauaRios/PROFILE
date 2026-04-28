from flask import Blueprint, render_template, abort

main = Blueprint('main', __name__)


@main.route('/')
def principal():
    return render_template('home.html')


@main.route('/projetos')
def projetos():
    # TODO: 
    return render_template('projetos.html')



@main.app_errorhandler(404)
def nao_encontrado(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def erro_interno(e):
    return render_template('500.html'), 500