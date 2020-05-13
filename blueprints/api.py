from flask import Blueprint
from flask_restful import Api

from resourses.user import User, Users

api_bp = Blueprint("api", __name__, url_prefix="/api")


class CustomApiErrorClass(Exception):
    @property
    def custom_data(self):
        return {'status': "failure", 'error': "None"}


api = Api(api_bp)

api.add_resource(User, "/users/<int:user_id>")
api.add_resource(Users, "/users")
