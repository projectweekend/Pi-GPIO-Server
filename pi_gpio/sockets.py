from flask.ext.socketio import send, emit
from pi_gpio import socketio
from config.pins import PinManager


def pin_event_response(pin_num, data):
    socketio.emit("pin:event", data)


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
            pin_event_response(pin_num, data)

        edge = self.gpio.__getattribute__(event)
        self.gpio.add_event_detect(num, edge, callback=event_callback, bouncetime=bounce)

    def read_all(self):
        results = []
        for pin_num, pin_config in self.pins.items():
            data = self.pin_response(pin_num, pin_config['mode'])
            results.append(data)
        return results

    def read_one(self, num):
        pin_num = int(num)
        try:
            pin_config = self.pins[pin_num]
            return self.pin_response(pin_num, pin_config['mode'])
        except KeyError:
            return None

    def update_value(self, num, value):
        pin_num = int(num)
        try:
            self.pins[pin_num]
            self.gpio.output(pin_num, value)
            return True
        except KeyError:
            return None


SOCKET_MANAGER = PinSocketManager()


@socketio.on('pin:list')
def pin_list():
    response = SOCKET_MANAGER.read_all()
    emit('pin:list', response)


@socketio.on('pin:read')
def pin_read(data):
    response = SOCKET_MANAGER.read_one(data.num)
    emit('pin:read', response)


@socketio.on('pin:write')
def pin_write(data):
    result = SOCKET_MANAGER.update_value(data.num, data.value)
    if not result:
        emit('pin:write', {'message': 'Pin not found'})
    else:
        response = SOCKET_MANAGER.read_one(data.num)
        emit('pin:write', response)
