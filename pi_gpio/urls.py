import time
from pi_gpio import app, socketio
from threading import Thread
from flask.ext import restful
from flask import render_template
from handlers import PinList, PinDetail


api = restful.Api(app)
api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')

THREAD = None


def background_thread():
    count = 0
    while True:
        time.sleep(5)
        count += 1
        socketio.emit('test', {'data': 'Server generated event', 'count': count})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    global THREAD
    if THREAD is None:
        THREAD = Thread(target=background_thread)
        THREAD.start()
    return render_template('index.html')
