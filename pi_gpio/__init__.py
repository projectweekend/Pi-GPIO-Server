import os
from flask import Flask
from flask import render_template
from flask.ext.socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['HOST'] = os.getenv('HOST', '0.0.0.0')
app.config['PORT'] = os.getenv('PORT', 3000)
app.config['DEBUG_MODE'] = os.getenv('DEBUG_MODE', True)

socketio = SocketIO(app)


import urls
import sockets


@app.route("/")
def index():
    return render_template("index.html")
