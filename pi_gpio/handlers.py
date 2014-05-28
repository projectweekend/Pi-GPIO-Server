from flask.ext.restful import Resource


class PinList(Resource):

    def get(self):
        return {'hello': 'world'}


class PinDetail(Resource):

    def get(self, pin_num):
        return {'pin': pin_num}

    def put(self, pin_num):
        return {'pin': pin_num}
