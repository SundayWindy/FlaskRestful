from flask_restful import Resource
from resources import schema, ApiResponse

from models.query_models.comment_model import CommentQueryModel
from models.response_models.comment_model import ResponseCommentModel

from handlers.comment_handler import CommentHandler


class Comment(Resource):
    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def get(self, topic_id, post_id, comment_id) -> ApiResponse:
        comment = CommentHandler(topic_id, post_id, comment_id).get_comment()
        return ApiResponse().ok(comment)

    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def put(self, topic_id, post_id, comment_id) -> ApiResponse:
        kwargs = self.parsed_args
        comment = CommentHandler(topic_id, post_id, comment_id).update_comment(**kwargs)
        return ApiResponse().ok(comment)

    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def delete(self, topic_id, post_id, comment_id) -> ApiResponse:
        CommentHandler(topic_id, post_id, comment_id).delete_comment()
        return ApiResponse().ok()


class Comments(Resource):
    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def get(self, topic_id, post_id) -> ApiResponse:
        kwargs = self.parsed_args
        comments = CommentHandler(topic_id=topic_id, post_id=post_id).get_comments(**kwargs)

        return ApiResponse().ok(comments)

    @schema(query_model=CommentQueryModel, response_model=ResponseCommentModel)
    def post(self, topic_id, post_id) -> ApiResponse:
        kwargs = self.parsed_args
        comment = CommentHandler(topic_id=topic_id, post_id=post_id).create_comment(**kwargs)

        return ApiResponse().ok(comment)
