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
            "value": fields.Integer
        }


class PinList(Pin):

    def get(self):
        result = MANAGER.read_all()
        return self.response(result, 200)


class PinDetail(Pin):

    def get(self, pin_num):
        result = MANAGER.read(pin_num)
        if not result:
            return {'message': 'Pin not found'}, 404
        return self.response(result, 200)

    def patch(self, pin_num):
        self.parser.add_argument('value', type=int)
        args = self.parser.parse_args()
        result = MANAGER.update_value(pin_num, args['value'])
        if not result:
            return {'message': 'Pin not found'}, 404
        return self.response(MANAGER.read(pin_num), 200)
