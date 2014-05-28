from flask.ext.restful import Resource, reqparse, marshal, fields


class Pin(Resource):

    fields = {
        "status": fields.String
    }

    def response(self, data, code):
        return marshal(data, self.fields), code


class PinList(Pin):

    def get(self):
        return {'hello': 'world'}


class PinDetail(Pin):

    def get(self, pin_num):
        return {'pin': pin_num}

    def put(self, pin_num):
        return {'pin': pin_num}
