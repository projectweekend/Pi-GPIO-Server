from flask.ext.restful import fields
from meta import BasicResource


class Pin(BasicResource):

    def __init__(self):
        super(Pin, self).__init__()
        self.fields = {
            "status": fields.String
        }


class PinList(Pin):

    def get(self):
        return {'hello': 'world'}


class PinDetail(Pin):

    def get(self, pin_num):
        return {'pin': pin_num}

    def put(self, pin_num):
        return {'pin': pin_num}

    def patch(self, pin_num):
        pass
