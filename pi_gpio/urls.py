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


import time
import RPi.GPIO as GPIO

def background_thread():
    while True:
        GPIO.wait_for_edge(23, GPIO.RISING)
        socketio.emit('pin:event', {"message":"woohoo!"})
        time.sleep(0.5)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    global THREAD
    if THREAD is None:
        THREAD = Thread(target=background_thread)
        THREAD.start()
    return render_template('index.html')
