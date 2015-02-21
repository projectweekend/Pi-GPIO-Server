from flask.ext.restful import fields
from meta import BasicResource
from config.pins import PinHttpManager


HTTP_MANAGER = PinHttpManager()


class Pin(BasicResource):

    def __init__(self):
        super(Pin, self).__init__()
        self.fields = {
            "num": fields.Integer,
            "name": fields.String,
            "mode": fields.String,
            "value": fields.Integer,
            "resistor": fields.String,
            "initial": fields.String,
            "event": fields.String,
            "bounce": fields.Integer
        }

    def pin_not_found(self):
        return {'message': 'Pin not found'}, 404


class PinList(Pin):

    def get(self):
        result = HTTP_MANAGER.read_all()
        return self.response(result, 200)


class PinDetail(Pin):

    def get(self, pin_num):
        result = HTTP_MANAGER.read_one(pin_num)
        if not result:
            return self.pin_not_found()
        return self.response(result, 200)

    def patch(self, pin_num):
        self.parser.add_argument('value', type=int)
        args = self.parser.parse_args()
        result = HTTP_MANAGER.update_value(pin_num, args['value'])
        if not result:
            return self.pin_not_found()
        return self.response(HTTP_MANAGER.read_one(pin_num), 200)
