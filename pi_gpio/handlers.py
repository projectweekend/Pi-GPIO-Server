from flask.ext import restful


class PinList(restful.Resource):

    def get(self):
        return {'hello': 'world'}


class PinDetail(restful.Resource):

    def get(self, pin_num):
        return {'pin': pin_num}
