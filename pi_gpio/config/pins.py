import yaml
from .gpio import BaseGPIO
from pi_gpio import app
from pi_gpio import sockets

PINS_YML = './config/pins.yml'


class PinRestManager(BaseGPIO):

    def __init__(self):
        super(PinRestManager, self).__init__()
        self.load_yaml()
        self.initialize_pins()

    def load_yaml(self):
        with open(PINS_YML) as file_data:
            self.__pins = yaml.safe_load(file_data)

    def initialize_pins(self):
        for pin_num, pin_config in self.__pins.items():
            initial = pin_config.get('initial', 'LOW')
            resistor = pin_config.get('resistor', None)
            event = pin_config.get('event', None)
            self.setup_pin(pin_num, pin_config['mode'], initial, resistor)
            if event:
                self.add_event(pin_num, event, pin_config['bounce'])

    def setup_pin(self, num, mode, initial, resistor):
        mode = self.gpio.__getattribute__(mode)
        initial = self.gpio.__getattribute__(initial)
        if resistor:
            resistor = self.gpio.__getattribute__(resistor)
            self.gpio.setup(num, mode, initial=initial, pull_up_down=resistor)
        else:
            self.gpio.setup(num, mode, initial=initial)

    def add_event(self, num, event, bounce):

        def event_callback(pin_num):
            pin_config = self.__pins[pin_num]
            value = 0
            if pin_config['event'] == 'RISING':
                value = 1
            response_data = self.pin_response(pin_num, pin_config['mode'], value)
            print(response_data)
            with app.app_context():
                sockets.pin_event_response(pin_num, response_data)

        edge = self.gpio.__getattribute__(event)
        self.gpio.add_event_detect(num, edge, callback=event_callback, bouncetime=bounce)

    def pin_response(self, num, mode, value=None):
        output = {
            'num': num,
            'mode': mode
        }
        if value:
            output['value'] = value
        else:
            output['value'] = self.gpio.input(num)
        return output

    def read_all(self):
        results = []
        for pin_num, pin_config in self.__pins.items():
            data = self.pin_response(pin_num, pin_config['mode'])
            results.append(data)
        return results

    def read_one(self, num):
        pin_num = int(num)
        try:
            pin_config = self.__pins[pin_num]
            return self.pin_response(pin_num, pin_config['mode'])
        except KeyError:
            return None

    def update_value(self, num, value):
        pin_num = int(num)
        try:
            self.__pins[pin_num]
            self.gpio.output(pin_num, value)
            return True
        except KeyError:
            return None
