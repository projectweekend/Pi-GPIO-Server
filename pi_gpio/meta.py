from flask.ext.restful import Resource, marshal, reqparse


class BasicResource(Resource):

    def __init__(self):
        super(BasicResource, self).__init__()
        self.parser = reqparse.RequestParser()

    def response(self, data, code):
        return marshal(data, self.fields), code
