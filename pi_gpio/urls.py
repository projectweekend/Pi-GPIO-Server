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


THREAD = None


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    global THREAD
    if THREAD is None:
        for event_func in event_manager.events:
            t = Thread(target=event_func)
            t.start()
            print("Thread launched")
    THREAD = True
    return render_template('index.html')
