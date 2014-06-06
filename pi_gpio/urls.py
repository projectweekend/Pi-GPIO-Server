import yaml
from pi_gpio import app, socketio
from flask.ext import restful
from flask import render_template
import RPi.GPIO as GPIO
from handlers import PinList, PinDetail


api = restful.Api(app)
api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')

PINS_YML = './config/pins.yml'
EDGE = {
    'RISING': GPIO.RISING,
    'FALLING': GPIO.FALLING,
    'BOTH': GPIO.BOTH
}
PINS = None


def read_pin_config():
    with open(PINS_YML) as file_data:
        pins = yaml.safe_load(file_data)
    return pins


def build_callback(num, event):
    def event_callback(num):
        data = {
            'num': num,
            'event': event
        }
        socketio.emit('pin:event', data)
        print(data)
    return event_callback


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    global PINS
    if PINS is None:
        PINS = read_pin_config()
        for num, config in PINS.items():
            event = config.get('event', None)
            if event:
                bounce = config['bounce']
                edge = EDGE[event]
                callback = build_callback(num, event)
                GPIO.add_event_detect(num, edge, callback=callback, bouncetime=bounce)
    return render_template('index.html')
