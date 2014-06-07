from pi_gpio import app
from flask.ext import restful
from flask import render_template
from handlers import PinList, PinDetail
from events import PinEventManager


EVENT_MANAGER = None

api = restful.Api(app)
api.add_resource(PinList, '/api/v1/pin')
api.add_resource(PinDetail, '/api/v1/pin/<string:pin_num>')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    global EVENT_MANAGER
    if EVENT_MANAGER is None:
        EVENT_MANAGER = PinEventManager()
        EVENT_MANAGER.register_gpio_events()
    return render_template('index.html')
