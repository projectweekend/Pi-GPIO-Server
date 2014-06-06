import time
from config.pins import PinManager


class PinEventManager(PinManager):

    def __init__(self, socketio):
        super(PinEventManager, self).__init__()
        self.events = []
        self.build_events(socketio)

    def build_events(self, socketio):
        for pin_num, pin_config in self.pins.items():
            event = pin_config.get('event', None)
            if event:
                self.add_event(pin_num, event, pin_config['bounce'], socketio)

    def add_event(self, num, event, bounce, socketio):

        def event_function():
            edge = self.gpio.__getattribute__(event)
            while True:
                self.gpio.wait_for_edge(num, edge)
                data = {
                    'num': num,
                    'event': event
                }
                socketio.emit("pin:event", data)
                time.sleep(bounce * 0.001)

        print("Added event for pin: {0}".format(num))
        self.events.append(event_function)
