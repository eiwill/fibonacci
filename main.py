import werkzeug.serving

from gevent.pywsgi import WSGIServer
from fibonacci.frontend import app


@werkzeug.serving.run_with_reloader
def run_server():
    """
    Start the server on port from config if it hasn't been
    already started and wait until it's stopped.
    This function is used only for development mode.
    """
    http_server = WSGIServer(('', app.config["LISTEN_PORT"]), app)
    http_server.serve_forever()


if __name__ == "__main__":
    run_server()
