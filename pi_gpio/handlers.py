from flask.ext.restful import fields
from meta import BasicResource
from config.pins import PinManager

MANAGER = PinManager()


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
        return self.response(MANAGER.pins, 200)


class PinDetail(Pin):

    def get(self, pin_num):
        output = MANAGER.read(pin_num)
        if not output:
            return {'message': 'Pin not found'}, 404
        return self.response(output, 200)

    def put(self, pin_num):
        return {'pin': pin_num}

    def patch(self, pin_num):
        pass
