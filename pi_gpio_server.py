from pi_gpio import app, socketio


HOST = app.config['HOST']
PORT = app.config['PORT']


if __name__ == '__main__':
    socketio.run(app, host=HOST, port=PORT)
