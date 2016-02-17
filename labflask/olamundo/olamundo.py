#!/usr/bin/env python
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def olamundo():
    return 'Olá Mundo!'


@app.route('/<nome>', methods=['GET'])
def parametro_url(nome):
    return 'Olá, {}'.format(nome)


@app.route('/idade/<int:idade>', methods=['GET'])
def auto_casting_parametro(idade):
    return 'Idade: {} | próxima: {!r}'.format(idade, idade + 1)


@app.route('/rota1', methods=['GET'])
@app.route('/rota2', methods=['GET'])
@app.route('/rota3', methods=['GET'])
@app.route('/rota4', methods=['GET'])
def funcao_varias_rotas():
    return 'Acessou pela rota: {!r}'.format(flask.request.path)


@app.route('/meu/ip', methods=['GET'])
def meu_ip():
    return 'Meu IP é: {}'.format(flask.request.remote_addr)


@app.route('/meu/navegador', methods=['GET'])
def meu_navegador():
    return 'Meu navegador é: {}'.format(flask.request.user_agent)


@app.route('/ola_post', methods=['GET', 'POST'])
def ola_post():

    if flask.request.method == 'GET':
        return 'Informe o nome via HTTP/POST'
    elif flask.request.method == 'POST':
        return 'Olá, {}'.format(flask.request.form.get('nome', '<sem nome>'))

    return 'Não te conheço.'

if __name__ == '__main__':
    app.run(debug=True)
