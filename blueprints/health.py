from flask import Blueprint
from flask_restful import Api, Resource


class HealthState(Resource):
    def get(self):
        return {"state": "OK"}, 200


class FaviconIco(Resource):
    def get(self):
        return {}, 200


health_bp = Blueprint("health", __name__, url_prefix='')

api = Api(health_bp)
api.add_resource(HealthState, "/health")
api.add_resource(FaviconIco, "/favicon.ico")
