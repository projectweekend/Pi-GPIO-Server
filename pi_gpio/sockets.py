from flask.ext.socketio import emit
from pi_gpio import socketio, app
from config.pins import PinManager


def pin_event_response(pin_num, data):
    route = "pin:{0}".format(pin_num)
    emit(route, data)


class PinSocketManager(PinManager):

    def __init__(self):
        super(PinSocketManager, self).__init__()
        self.initialize_pins()

    def initialize_pins(self):
        for pin_num, pin_config in self.pins.items():
            event = pin_config.get('event', None)
            if event:
                print("Adding event")
                self.add_event(pin_num, event, pin_config['bounce'])

    def add_event(self, num, event, bounce):

        def event_callback(pin_num):
            pin_config = self.pins[pin_num]
            value = 0
            if pin_config['event'] == 'RISING':
                value = 1
            data = self.pin_response(pin_num, pin_config['mode'], value)
            print(data)
            with app.request_context():
                pin_event_response(pin_num, data)

        edge = self.gpio.__getattribute__(event)
        self.gpio.add_event_detect(num, edge, callback=event_callback, bouncetime=bounce)


PinSocketManager()
