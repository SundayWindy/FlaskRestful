from exceptions.exceptions import ArgumentInvalid, ObjectsNotExist
from typing import Generator, Optional

from sqlalchemy import and_

from configures.const import POST_MINIMUM_WORDS
from handlers import BaseHandler
from models.database_models import Comment
from models.database_models.post_model import Post
from models.database_models.topic_model import Topic
from models.database_models.user_model import User
from models.response_models.post_model import ResponsePostModel


class PostHandler(BaseHandler):
    _model = Post

    def __init__(self, topic_id: int = None, post_id: int = None) -> None:
        super().__init__(post_id)
        self.topic_id = topic_id
        self.error_msg = f"Post <{id}> 不存在"

    def assert_topic_id_is_not_none(self) -> None:
        if self.topic_id is None:
            raise ArgumentInvalid("topic_id 不能为 None")

    def assert_topic_exist(self) -> None:
        ins = Topic.query.filter_by(deleted=False).filter_by(id=self.topic_id).first()
        if not ins:
            raise ObjectsNotExist(f"Topic <{self.topic_id}> 不存在")

    @staticmethod
    def assert_user_exist(user_id: int) -> None:
        ins = User.query.filter_by(deleted=False).filter_by(id=user_id).first()
        if not ins:
            raise ObjectsNotExist(f"User <{user_id}> 不存在")

    def assert_post_id_is_not_none(self) -> None:
        if self.id is None:
            raise ArgumentInvalid("post_id 不能为 None")

    @staticmethod
    def get_comment_count(instance: Comment) -> int:
        condition = and_(Comment.deleted == False, Comment.post_id == instance.id)  # noqa
        total = Comment.query.filter(condition).count()

        return total

    def get_post(self) -> ResponsePostModel:
        self.assert_post_id_is_not_none()

        post = self._get_sqlalchemy_instance()
        post.update(click_times=post.click_times + 1)

        comments_count = self.get_comment_count(post)
        return ResponsePostModel(comments_count=comments_count, **post.as_dict())

    def get_posts(self, **kwargs) -> Generator[ResponsePostModel, None, None]:
        self.assert_topic_id_is_not_none()
        per_page = kwargs["per_page"]
        offset = kwargs["offset"]

        condition = and_(Post.deleted == False, Post.topic_id == self.topic_id)  # noqa
        posts = self._model.query.filter(condition).offset(offset).limit(per_page)  # 分页
        for post in posts:
            post.update(click_times=post.click_times or 0 + 1)
            comments_count = self.get_comment_count(post)
            yield ResponsePostModel(comments_count=comments_count, **post.as_dict())

    def create_post(self, **kwargs) -> Optional[ResponsePostModel]:
        self.assert_topic_id_is_not_none()
        self.assert_topic_exist()

        user_id = kwargs["user_id"]
        self.assert_user_exist(user_id)

        content = kwargs["content"]
        if content is None or len(content.strip()) <= POST_MINIMUM_WORDS:
            raise ArgumentInvalid(f"Post 文章字数不能少于 <{POST_MINIMUM_WORDS}> 个")
        post = self._model.create(topic_id=self.topic_id, **kwargs)

        return ResponsePostModel(comments_count=0, **post.as_dict())

    def update_post(self, **kwargs) -> ResponsePostModel:
        self.assert_topic_id_is_not_none()
        self.assert_topic_exist()

        user_id = kwargs["user_id"]
        self.assert_user_exist(user_id)

        post = self._get_sqlalchemy_instance()
        post.update(**kwargs)

        return self.get_post()

    def delete_post(self) -> None:
        instance = self._get_sqlalchemy_instance()
        instance.update(deleted=True)

        return
