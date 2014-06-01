import yaml
from .gpio import BaseGPIO

PINS_YML = './config/pins.yml'


class Config(BaseGPIO):

    def __init__(self):
        super(Config, self).__init__()
        self.load_from_yaml()
        # self.initialize_pins()

    def load_from_yaml(self):
        with open(PINS_YML) as file_data:
            self.pins = yaml.safe_load(file_data)

    def initialize_pins(self):
        for pin in self.pins:
            initial = pin.get('initial', 'LOW')
            resistor = pin.get('resistor', None)
            self.setup_pin(pin['num'], pin['mode'], initial, resistor)

    def setup_pin(self, num, mode, initial, resistor):
        mode = self.gpio.__getattribute__(mode)
        initial = self.gpio.__getattribute__(initial)
        if resistor:
            resistor = self.gpio.__getattribute__(resistor)
            self.gpio.setup(num, mode, initial=initial, pull_up_down=resistor)
        else:
            self.gpio.setup(num, mode, initial=initial)
