from pi_gpio import app, socketio
from flask.ext import restful
from flask import render_template
from handlers import PinList, PinDetail


api = restful.Api(app)
api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')

import RPi.GPIO as GPIO


def event_callback(pin):
    socketio.emit('pin:event', {"message":"woohoo!"})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    GPIO.add_event_detect(23, GPIO.RISING, callback=event_callback)
    return render_template('index.html')
