import os
from flask import Flask
from flask.ext.socketio import SocketIO
from gevent import monkey


monkey.patch_all()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', "TEST")
app.config['HOST'] = os.getenv('HOST', '0.0.0.0')
app.config['PORT'] = os.getenv('PORT', 5000)
# app.debug = os.getenv('DEBUG', False)
app.debug = True

socketio = SocketIO(app)


import urls
import sockets
