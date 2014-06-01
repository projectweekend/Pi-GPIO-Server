from flask.ext.restful import fields
from meta import BasicResource
from config.pins import Config

CONFIG = Config()


class Pin(BasicResource):

    def __init__(self):
        super(Pin, self).__init__()
        self.fields = {
            "num": fields.Integer,
            "mode": fields.String,
            "initial": fields.String,
            "resistor": fields.String
        }


class PinList(Pin):

    def get(self):
        return self.response(CONFIG.pins, 200)


class PinDetail(Pin):

    def get(self, pin_num):
        return {'pin': pin_num}

    def put(self, pin_num):
        return {'pin': pin_num}

    def patch(self, pin_num):
        pass
