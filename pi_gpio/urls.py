from pi_gpio import app
from flask.ext import restful
from flask import render_template
from handlers import PinList, PinDetail


@app.route('/')
def index():
    return render_template('index.html')


api = restful.Api(app)

api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')
