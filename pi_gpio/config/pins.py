import yaml
from .gpio import BaseGPIO

PINS_YML = './config/pins.yml'


class Config(BaseGPIO):

    def __init__(self):
        super(Config, self).__init__()
        self.__load_from_yaml()
        self.__initialize_pins()

    def __load_from_yaml(self):
        with open(PINS_YML) as file_data:
            self.pins = yaml.safe_load(file_data)

    def __initialize_pins(self):
        for pin in self.pins:
            initial = pin.get('initial', 'LOW')
            resistor = pin.get('resistor', None)
            self.__setup_pin(pin['num'], pin['mode'], initial, resistor)

    def __setup_pin(self, num, mode, initial, resistor):
        mode = self.__gpio.__getattribute__(mode)
        initial = self.__gpio.__getattribute__(initial)
        if resistor:
            resistor = self.__gpio.__getattribute__(resistor)
            self.__gpio.setup(num, mode, initial=initial, pull_up_down=resistor)
        else:
            self.__gpio.setup(num, mode, initial=initial)
