import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class BaseGPIO(object):

    def __init__(self):
        self.gpio = GPIO
