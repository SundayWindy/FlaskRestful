import datetime
import json
import logging
import os
import socket
import traceback
import types
from logging.config import dictConfig
from typing import Any, Dict, Tuple, Union

from flask import Flask, request
from flask_cors import CORS
from pyruicore import BaseModel
from werkzeug.exceptions import HTTPException

from blueprints import all_blueprints
from configures import settings
from exceptions.exceptions import ServerException
from exceptions.send_alert import send_dingding_alert
from models.orm import db
from resources import ApiResponse

# from models.base import BaseModel


logger = logging.getLogger(__name__)


class JsonEncoder(json.JSONEncoder):
    def default(self, value) -> Any:
        if isinstance(value, (datetime.datetime, datetime.date)):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(value, ApiResponse):
            return value.get()
        if isinstance(value, BaseModel):
            return value.dict()
        if isinstance(value, types.GeneratorType):
            return [self.default(v) for v in value]

        return json.JSONEncoder.default(self, value)


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    init_config(app)

    app.json_encoder = JsonEncoder
    return app


def init_config(app) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    register_blueprints(app)
    app.register_error_handler(Exception, handle_exception)

    db.init_app(app)

    return


def register_blueprints(app) -> None:
    for blueprint in all_blueprints:
        app.register_blueprint(blueprint)

    return


def handle_exception(e) -> Tuple[Dict[str, Union[Union[int, str, list], Any]], Union[int, Any]]:
    code = 500
    if isinstance(e, (HTTPException, ServerException)):
        code = e.code

    logger.exception(e)
    exc = [v for v in traceback.format_exc(limit=10).split("\n")]
    if str(code) == "500":
        send_dingding_alert(request.url, request.args, request.json, repr(e), exc)
    return {"error_code": code, "error_msg": str(e), "traceback": exc}, code


def init_logging() -> None:
    level = "INFO" if settings.NAMESPACE == "PRODUCTION" else "DEBUG"
    dir_name = "./logs/{}".format(socket.gethostname())
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "brief": {"format": "%(message)s"},
            "standard": {
                "format": "[%(asctime)s] [%(levelname)s] [%(filename)s.%(funcName)s:%(lineno)3d] [%(process)d::%("
                "thread)d] %(message)s "
            },
            "colored": {
                "()": "colorlog.ColoredFormatter",
                "format": "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "log_colors": {
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                },
            },
        },
        "handlers": {
            "default": {
                "level": level,
                "formatter": "standard",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "{}/server.log".format(dir_name),
                "when": "midnight",
                "interval": 1,
                "encoding": "utf8",
            },
            "console": {"level": level, "formatter": "colored", "class": "logging.StreamHandler"},
            "default_access": {
                "level": level,
                "formatter": "brief",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "{}/access.log".format(dir_name),
                "when": "midnight",
                "interval": 1,
                "encoding": "utf8",
            },
            "console_access": {
                "level": level,
                "formatter": "colored",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "werkzeug": {
                "handlers": ["default_access", "console_access"],
                "level": level,
                "propagate": False,
            },
            "": {
                "handlers": ["default", "console"],
                "formatter": "colored",
                "level": level,
                "propagate": True,
            },
        },
    }

    def patch_wsgi_handler():
        """
        忽略WSGIServer log标签
        """
        from gevent.pywsgi import WSGIHandler

        logger = logging.getLogger("werkzeug")

        def log_request(self):
            logger.info(WSGIHandler.format_request(self))

        WSGIHandler.log_request = log_request

    dictConfig(config)
    patch_wsgi_handler()
