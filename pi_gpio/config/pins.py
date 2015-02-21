import yaml
from .gpio import BaseGPIO


PINS_YML = './config/pins.yml'


class PinManager(BaseGPIO):

    def __init__(self):
        super(PinManager, self).__init__()
        self.load_yaml()

    def load_yaml(self):
        with open(PINS_YML) as file_data:
            self.pins = yaml.safe_load(file_data)

    def pin_response(self, num, config):
        output = {
            'num': num,
            'name': config.get('name', ''),
            'mode': config['mode'],
            'value': self.gpio.input(num)
        }
        resistor = config.get('resistor', None)
        if resistor:
            output['resistor'] = resistor
        initial = config.get('initial', None)
        if initial:
            output['initial'] = initial
        event = config.get('event', None)
        if event:
            output['event'] = event
        bounce = config.get('bounce', None)
        if bounce:
            output['bounce'] = bounce
        return output

    def read_all(self):
        results = []
        for pin_num, pin_config in self.pins.items():
            data = self.pin_response(pin_num, pin_config)
            results.append(data)
        return results

    def read_one(self, num):
        pin_num = int(num)
        try:
            pin_config = self.pins[pin_num]
            return self.pin_response(pin_num, pin_config)
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


class PinHttpManager(PinManager):

    def __init__(self):
        super(PinHttpManager, self).__init__()
        self.initialize_pins()

    def initialize_pins(self):
        for pin_num, pin_config in self.pins.items():
            initial = pin_config.get('initial', 'LOW')
            resistor = pin_config.get('resistor', None)
            self.setup_pin(pin_num, pin_config['mode'], initial, resistor)

    def setup_pin(self, num, mode, initial, resistor):
        mode = self.gpio.__getattribute__(mode)
        initial = self.gpio.__getattribute__(initial)
        if resistor:
            resistor = self.gpio.__getattribute__(resistor)
            self.gpio.setup(num, mode, initial=initial, pull_up_down=resistor)
        else:
            self.gpio.setup(num, mode, initial=initial)
