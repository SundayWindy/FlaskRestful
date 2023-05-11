from flask import Blueprint
from flask_restful import Api

from authentication.token import Token
from resources.comment import Comment, Comments
from resources.post import Post, Posts
from resources.topic import RootTopic, RootTopics, Topic, Topics
from resources.user import User, Users

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp, errors=Exception)

api.add_resource(User, '/users/<int:user_id>')
api.add_resource(Users, '/users')

api.add_resource(Topic, '/topics/<int:topic_id>')
api.add_resource(Topics, '/topics')

api.add_resource(RootTopic, '/root_topics/<int:root_topic_id>')
api.add_resource(RootTopics, '/root_topics')

api.add_resource(Post, '/topics/<int:topic_id>/posts/<int:post_id>')
api.add_resource(Posts, '/topics/<int:topic_id>/posts')

api.add_resource(Comment, '/topics/<int:topic_id>/posts/<int:post_id>/comments/<int:comment_id>')
api.add_resource(Comments, '/topics/<int:topic_id>/posts/<int:post_id>/comments')

api.add_resource(Token, '/token')
