import flask

from . import app


@app.route('/jinja/ola_mundo')
def ola_mundo():
    return flask.render_template('ola_mundo.html')
