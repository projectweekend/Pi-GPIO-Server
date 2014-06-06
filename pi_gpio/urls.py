from pi_gpio import app, socketio
from threading import Thread
from flask.ext import restful
from flask import render_template
from handlers import PinList, PinDetail
from events import PinEventManager


api = restful.Api(app)
api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')
event_manager = PinEventManager(socketio)


THREADS = []


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    global THREADS
    if len(THREADS) == 0:
        for event_func in event_manager.events:
            t = Thread(target=event_func)
            t.start()
            THREADS.append(t)
    return render_template('index.html')
