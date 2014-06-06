from pi_gpio import app, socketio
from flask.ext import restful
from flask import render_template
import RPi.GPIO as GPIO
from handlers import PinList, PinDetail
from config.pins import PinManager


api = restful.Api(app)
api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')

EDGE = {
    'RISING': GPIO.RISING,
    'FALLING': GPIO.FALLING,
    'BOTH': GPIO.BOTH
}
EVENT_MANAGER = None


def build_callback(num, event, socketio):
    def event_callback(num):
        data = {
            'num': num,
            'event': event
        }
        print(data)
        socketio.emit('pin:event', data)
    print("Callback built for: {0}".format(num))
    return event_callback


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    global EVENT_MANAGER
    if EVENT_MANAGER is None:
        EVENT_MANAGER = PinManager()
        # for pin_num, pin_config in EVENT_MANAGER.pins.items():
        #     bounce = pin_config['bounce']
        #     event = pin_config.get('event', None)
        #     if event:
        #         edge = EDGE[event]
        #         callback = build_callback(pin_num, event, socketio)
        #         GPIO.add_event_detect(pin_num, edge, callback=callback, bouncetime=bounce)
    return render_template('index.html')
