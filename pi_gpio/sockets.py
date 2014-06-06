from flask.ext.socketio import emit
from pi_gpio import socketio
from config.pins import PinManager


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
            socketio.emit("pin:event", data)

        edge = self.gpio.__getattribute__(event)
        self.gpio.add_event_detect(num, edge, callback=event_callback, bouncetime=bounce)


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
