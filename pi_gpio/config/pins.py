import yaml
from .gpio import BaseGPIO

PINS_YML = './config/pins.yml'


class PinManager(BaseGPIO):

    def __init__(self):
        super(PinManager, self).__init__()
        self.pins = []
        self.load_yaml()
        self.initialize_pins()

    def load_yaml(self):
        with open(PINS_YML) as file_data:
            self.__pins = yaml.safe_load(file_data)

    def initialize_pins(self):
        for pin in self.__pins:
            initial = pin.get('initial', 'LOW')
            resistor = pin.get('resistor', None)
            self.setup_pin(pin['num'], pin['mode'], initial, resistor)
            self.pins.append({
                'num': pin['num'],
                'mode': pin['mode'],
                'initial': initial,
                'resistor': resistor
            })

    def setup_pin(self, num, mode, initial, resistor):
        mode = self.gpio.__getattribute__(mode)
        initial = self.gpio.__getattribute__(initial)
        if resistor:
            resistor = self.gpio.__getattribute__(resistor)
            self.gpio.setup(num, mode, initial=initial, pull_up_down=resistor)
        else:
            self.gpio.setup(num, mode, initial=initial)

    def read_all(self):
        results = []
        for pin in self.pins:
            pin_read = pin.copy()
            pin_read['value'] = self.gpio.input(pin['num'])
            results.append(pin_read)
        return results

    def read(self, num):
        for pin in self.pins:
            if int(num) == pin['num']:
                pin_read = pin.copy()
                pin_read['value'] = self.gpio.input(pin['num'])
                return pin_read
        return None

    def update(self, num, value):
        self.gpio.output(int(num), value)
        self.read(num)
