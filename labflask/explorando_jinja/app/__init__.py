import flask

app = flask.Flask(__name__)

from .views import *
