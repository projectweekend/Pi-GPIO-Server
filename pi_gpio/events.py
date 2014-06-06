from config.pins import PinManager


class PinEventManager(PinManager):

    def __init__(self, socketio):
        super(PinEventManager, self).__init__()
        self.socketio = socketio
        self.build_events()

    def build_events(self):
        for pin_num, pin_config in self.pins.items():
            event = pin_config.get('event', None)
            if event:
                self.add_event(pin_num, event, pin_config['bounce'])

    def add_event(self, num, event, bounce):

        edge = self.gpio.__getattribute__(event)

        def event_callback():
            data = {
                'num': num,
                'event': event
            }
            self.socketio.emit('pin:event', data)

        self.gpio.add_event_detect(num, edge, callback=event_callback, bouncetime=bounce)
