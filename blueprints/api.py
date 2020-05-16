from flask import Blueprint
from flask_restful import Api

from resources.post import Post, Posts
from resources.topic import Topic, Topics
from resources.user import User, Users

api_bp = Blueprint("api", __name__, url_prefix="/api")

api = Api(api_bp, errors=Exception)

api.add_resource(User, "/users/<int:user_id>")
api.add_resource(Users, "/users")

api.add_resource(Topic, "/topics/<int:topic_id>")
api.add_resource(Topics, "/topics")

api.add_resource(Post, "/topics/<int:topic_id>/posts/<int:post_id>")
api.add_resource(Posts, "/topics/<int:topic_id>/posts")
