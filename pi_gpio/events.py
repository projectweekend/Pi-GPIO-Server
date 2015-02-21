from pi_gpio import socketio
from config.pins import PinManager


class PinEventManager(PinManager):

    def __init__(self):
        super(PinEventManager, self).__init__()
        self.socketio = socketio
        self.edge = {
            'RISING': self.gpio.RISING,
            'FALLING': self.gpio.FALLING,
            'BOTH': self.gpio.BOTH
        }

    def build_event_callback(self, num, name, event):
        def event_callback(num):
            data = {
                'num': num,
                'name': name,
                'event': event
            }
            self.socketio.emit('pin:event', data)
            print(data)
        return event_callback

    def register_gpio_events(self):
        for num, config in self.pins.items():
            event = config.get('event', None)
            name = config.get('name', '')
            if event:
                edge = self.edge[event]
                bounce = config['bounce']
                cb = self.build_event_callback(num, name, event)
                self.gpio.add_event_detect(num, edge, callback=cb, bouncetime=bounce)
