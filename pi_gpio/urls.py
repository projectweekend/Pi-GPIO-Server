from pi_gpio import app, socketio
from flask.ext import restful
from flask import render_template
import RPi.GPIO as GPIO
from handlers import PinList, PinDetail
from events import PinEventManager


api = restful.Api(app)
api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')

EDGE = {
    'RISING': GPIO.RISING,
    'FALLING': GPIO.FALLING,
    'BOTH': GPIO.BOTH
}
EVENT_MANAGER = None


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    global EVENT_MANAGER
    if EVENT_MANAGER is None:
        EVENT_MANAGER = PinEventManager(socketio)
        for pin_num, pin_config in EVENT_MANAGER.pins.items():
            bounce = pin_config['bounce']
            event = pin_config.get('event', None)
            if event:
                edge = EDGE[event]
                callback = EVENT_MANAGER.build_callback(pin_num, event, bounce)
                GPIO.add_event_detect(pin_num, edge, callback=callback, bouncetime=bounce)
    return render_template('index.html')
