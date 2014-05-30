from flask.ext.socketio import emit
from pi_gpio import socketio


@socketio.on('test')
def test_socket(data):
    emit('test', {'message': "test"})
