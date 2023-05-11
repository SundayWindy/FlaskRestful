from typing import Generator, Optional

from sqlalchemy import and_

from configures.const import PER_PAGE
from exceptions.exceptions import ActionNotAllowed, ArgumentInvalid, ObjectsNotExist
from handlers import BaseHandler
from handlers.utils import ContentChecker
from models.database_models.comment_model import Comment
from models.database_models.post_model import Post
from models.database_models.topic_model import Topic
from models.database_models.user_model import User
from models.response_models.comment_model import ResponseCommentModel


class CommentHandler(BaseHandler):
    _model = Comment

    def __init__(self, topic_id=None, post_id=None, id=None) -> None:
        super().__init__(id)
        self.topic_id = topic_id
        self.post_id = post_id
        self.error_msg = f'Comment <{id}> 不存在'

    def assert_post_exist(self) -> None:
        self.assert_topic_exist()
        if self.post_id is None:
            raise ArgumentInvalid('post_id 不能为 None')
        post = Post.query.filter_by(deleted=False).filter_by(id=self.post_id).first()
        if not post:
            raise ObjectsNotExist(f'Post <{self.post_id}> 不存在')

    def assert_topic_exist(self) -> None:
        if self.topic_id is None:
            return
        topic = Topic.query.filter_by(deleted=False).filter_by(id=self.topic_id).first()
        if not topic:
            raise ObjectsNotExist(f'Topic <{self.topic_id}> 不存在')

    @staticmethod
    def assert_user_exist(user_id: int) -> None:
        if user_id is None:
            raise ArgumentInvalid('user_id 不能为 None')
        user = User.query.filter_by(deleted=False).filter_by(id=user_id).first()
        if not user:
            raise ObjectsNotExist(f'Post <{user_id}> 不存在')

    def get_comment(self) -> ResponseCommentModel:
        instance = self._get_sqlalchemy_instance()
        return ResponseCommentModel(**instance.as_dict())

    def get_comments(self, **kwargs) -> Generator[ResponseCommentModel, None, None]:
        self.assert_post_exist()

        per_age = kwargs.get('per_page', PER_PAGE)
        offset = kwargs.get('offset', 0)
        condition = and_(Comment.deleted == False, Comment.post_id == self.post_id)
        comments = Comment.query.filter(condition).offset(offset).limit(per_age)

        yield from (ResponseCommentModel(**comment.as_dict()) for comment in comments)

    def create_comment(self, **kwargs) -> Optional[ResponseCommentModel]:
        self.assert_post_exist()
        user_id = kwargs.get('user_id')
        self.assert_user_exist(user_id)

        content = kwargs.get('content')
        if not ContentChecker.is_allowed(content):
            raise ArgumentInvalid(ContentChecker.ERROR_MSG)

        kwargs['post_id'] = self.post_id
        instance = self._model.create(**kwargs)

        return ResponseCommentModel(**instance.as_dict())

    def update_comment(self, **kwargs) -> Optional[ResponseCommentModel]:
        raise ActionNotAllowed('This operation is not allowed')

    def delete_comment(self) -> None:
        raise ActionNotAllowed('This operation is not allowed')
