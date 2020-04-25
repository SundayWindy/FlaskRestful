from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint("api", __name__, url_prefix="/api/")


class CustomApiErrorClass(Exception):
    @property
    def custom_data(self):
        return {'status': "failure", 'error': "NOne"}


api = Api(api_bp)
