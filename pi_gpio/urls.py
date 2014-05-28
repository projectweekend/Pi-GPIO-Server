from pi_gpio import app
from flask.ext import restful
from handlers import PinList, PinDetail


api = restful.Api(app)

api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')
