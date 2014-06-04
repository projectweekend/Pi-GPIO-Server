from gevent import monkey
monkey.patch_all()
import os
from flask import Flask
from flask.ext.socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', "TEST")
app.port = os.getenv('PORT', 5000)
app.debug = False

socketio = SocketIO(app)


import urls
import sockets
