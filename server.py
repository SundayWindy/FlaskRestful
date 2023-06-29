import logging

from gevent import monkey
from gevent.pywsgi import WSGIServer

from app import create_app, init_logging

monkey.patch_all()


def run(debug: bool = False):
    host = '0.0.0.0'
    port = 24579

    if debug:
        create_app().run(host=host, port=port, debug=debug)
    else:
        init_logging()
        http_server = WSGIServer((host, port), create_app())

        logging.getLogger(__name__).info('Server start at %s:%s' % (host, port))
        http_server.serve_forever()


if __name__ == '__main__':
    run(debug=False)
