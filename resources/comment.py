from flask_restful import Resource

from authentication import auth
from handlers.comment import CommentHandler
from models.query import CommentQueryModel
from models.response import ResponseCommentModel
from resources import ApiResponse, schema


class Comment(Resource):
    @auth.login_required
    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def get(self, topic_id, post_id, comment_id) -> ApiResponse:
        comment = CommentHandler(topic_id, post_id, comment_id).get_comment()
        return ApiResponse().ok(comment)

    @auth.login_required
    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def put(self, topic_id, post_id, comment_id) -> ApiResponse:
        kwargs = self.parsed_args
        comment = CommentHandler(topic_id, post_id, comment_id).update_comment(**kwargs)
        return ApiResponse().ok(comment)

    @auth.login_required
    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def delete(self, topic_id, post_id, comment_id) -> ApiResponse:
        CommentHandler(topic_id, post_id, comment_id).delete_comment()
        return ApiResponse().ok()


class Comments(Resource):
    @auth.login_required
    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def get(self, topic_id, post_id) -> ApiResponse:
        kwargs = self.parsed_args
        comments = CommentHandler(topic_id=topic_id, post_id=post_id).get_comments(**kwargs)

        return ApiResponse().ok(comments)

    @auth.login_required
    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def post(self, topic_id, post_id) -> ApiResponse:
        kwargs = self.parsed_args
        comment = CommentHandler(topic_id=topic_id, post_id=post_id).create_comment(**kwargs)

        return ApiResponse().ok(comment)
