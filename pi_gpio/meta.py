from flask.ext.restful import Resource, marshal


class BasicResource(Resource):

    def __init__(self):
        super(BasicResource, self).__init__()

    def response(self, data, code):
        return marshal(data, self.fields), code
