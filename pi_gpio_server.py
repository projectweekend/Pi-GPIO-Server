from pi_gpio import app


HOST = app.config['HOST']
PORT = app.config['PORT']
DEBUG_MODE = app.config['DEBUG']


if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host=HOST, port=PORT)
