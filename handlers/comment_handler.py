from sqlalchemy import and_

from handlers import BaseHandler

from models.database_models.comment_model import Comment
from models.database_models.post_model import Post
from models.database_models.user_model import User
from models.database_models.topic_model import Topic
from models.response_models.comment_model import ResponseCommentModel

from handlers.utils import ContentChecker
from configures.const import PER_PAGE

from exceptions import exceptions


class CommentHandler(BaseHandler):
    _model = Comment

    def __init__(self, topic_id=None, post_id=None, id=None):
        super().__init__(id)
        self.topic_id = topic_id
        self.post_id = post_id
        self.error_msg = f"Comment <{id}> 不存在"

    def assert_post_exist(self):
        self.assert_topic_exist()
        if self.post_id is None:
            raise exceptions.ArgumentInvalid("post_id 不能为 None")
        post = Post.query.filter_by(deleted=False).filter_by(id=self.post_id).first()
        if not post:
            raise exceptions.ObjectsNotExist(f"Post <{self.post_id}> 不存在")

    def assert_topic_exist(self):
        if self.topic_id is None:
            return
        topic = Topic.query.filter_by(deleted=False).filter_by(id=self.topic_id).first()
        if not topic:
            raise exceptions.ObjectsNotExist(f"Topic <{self.topic_id}> 不存在")

    @staticmethod
    def assert_user_exist(user_id):
        if user_id is None:
            raise exceptions.ArgumentInvalid("user_id 不能为 None")
        user = User.query.filter_by(deleted=False).filter_by(id=user_id).first()
        if not user:
            raise exceptions.ObjectsNotExist(f"Post <{user_id}> 不存在")

    def get_comment(self):
        instance = self._get_sqlalchemy_instance()
        return ResponseCommentModel(**instance.as_dict())

    def get_comments(self, **kwargs):
        self.assert_post_exist()

        per_age = kwargs.get("per_page", PER_PAGE)
        offset = kwargs.get("offset", 0)
        condition = and_(Comment.deleted == False, Comment.post_id == self.post_id)
        comments = Comment.query.filter(condition).offset(offset).limit(per_age)

        for comment in comments:
            yield ResponseCommentModel(**comment.as_dict())

    def create_comment(self, **kwargs):

        self.assert_post_exist()
        user_id = kwargs.get("user_id")
        self.assert_user_exist(user_id)

        content = kwargs.get("content")
        if not ContentChecker.is_allowed(content):
            raise exceptions.ArgumentInvalid(ContentChecker.ERROR_MSG)

        kwargs["post_id"] = self.post_id
        instance = self._model.create(**kwargs)

        return ResponseCommentModel(**instance.as_dict())

    def update_comment(self, **kwargs):
        raise exceptions.ActionNotAllowed("This operation is not allowed")

    def delete_comment(self):
        raise exceptions.ActionNotAllowed("This operation is not allowed")
