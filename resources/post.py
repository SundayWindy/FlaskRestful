from flask_restful import Resource

from authentication import auth
from handlers.post import PostHandler
from models.query import PostQueryModel
from models.response import ResponsePostModel
from resources import ApiResponse, schema


class Post(Resource):
    @auth.login_required
    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def get(self, topic_id, post_id) -> ApiResponse:
        post = PostHandler(topic_id=topic_id, post_id=post_id).get_post()
        return ApiResponse().ok(post)

    @auth.login_required
    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def put(self, topic_id, post_id) -> ApiResponse:
        kwargs = self.parsed_args
        post = PostHandler(topic_id, post_id).update_post(**kwargs)

        return ApiResponse().ok(post)

    @auth.login_required
    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def delete(self, topic_id, post_id) -> ApiResponse:
        PostHandler(topic_id, post_id).delete_post()

        return ApiResponse().ok()


class Posts(Resource):
    @auth.login_required
    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def get(self, topic_id) -> ApiResponse:
        kwargs = self.parsed_args
        posts = PostHandler(topic_id).get_posts(**kwargs)

        return ApiResponse().ok(posts)

    @auth.login_required
    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def post(self, topic_id) -> ApiResponse:
        kwargs = self.parsed_args
        post = PostHandler(topic_id).create_post(**kwargs)
        return ApiResponse().ok(post)
