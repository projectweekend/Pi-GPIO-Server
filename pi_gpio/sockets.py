from flask.ext.socketio import emit
from pi_gpio import socketio


@socketio.on('test')
def test_socket(data):
    emit('test', {'message': "test"})


def pin_event_response(pin_num, data):
    route = "pin:{0}".format(pin_num)
    emit(route, data)
