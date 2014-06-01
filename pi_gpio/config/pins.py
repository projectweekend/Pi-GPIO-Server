import yaml
from .gpio import BaseGPIO

PINS_YML = './config/pins.yml'


class PinManager(BaseGPIO):

    def __init__(self):
        super(PinManager, self).__init__()
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
        def event_cb(pin_num):
            print "Event on pin {0}!".format(pin_num)
        edge = self.gpio.__getattribute__(event)
        self.gpio.add_event_detect(num, edge, callback=event_cb, bouncetime=bounce)

    def read_all(self):
        results = []
        for pin_num, pin_config in self.__pins.items():
            results.append({
                'num': pin_num,
                'value': self.gpio.input(pin_num),
                'mode': pin_config['mode']
            })
        return results

    def read_one(self, num):
        pin_num = int(num)
        try:
            pin_config = self.__pins[pin_num]
            return {
                'num': pin_num,
                'value': self.gpio.input(pin_num),
                'mode': pin_config['mode']
            }
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
