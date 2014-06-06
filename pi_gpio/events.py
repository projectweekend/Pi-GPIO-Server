from config.pins import PinManager


class PinEventManager(PinManager):

    def __init__(self, socketio):
        super(PinEventManager, self).__init__()
        self.socketio = socketio

    def build_callback(self, num, event, bounce):
        def event_callback(num):
            data = {
                'num': num,
                'event': event
            }
            print(data)
            self.socketio.emit('pin:event', data)
        print("Callback built for: {0}".format(num))
        return event_callback
