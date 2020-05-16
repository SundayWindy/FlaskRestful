from exceptions import exceptions

from sqlalchemy import and_

from handlers import BaseHandler
from models.database_models.post_model import Post, Comment
from models.database_models.topic_model import Topic
from models.database_models.user_model import User
from models.response_models.post_model import ResponsePostModel

from configures.const import POST_MINIMUM_WORDS


class PostHandler(BaseHandler):
    _model = Post

    def __init__(self, topic_id=None, post_id=None):
        super().__init__(post_id)
        self.topic_id = topic_id
        self.error_msg = f"Post <{id}> 不存在"

    def assert_topic_id_is_not_none(self):
        if self.topic_id is None:
            raise exceptions.ArgumentInvalid("topic_id 不能为 None")

    def assert_topic_exist(self):
        ins = Topic.query.filter_by(deleted=False).filter_by(id=self.topic_id).first()
        if not ins:
            raise exceptions.ObjectsNotExist(f"Topic <{self.topic_id}> 不存在")

    def assert_user_exist(self, user_id):
        ins = User.query.filter_by(deleted=False).filter_by(id=user_id).first()
        if not ins:
            raise exceptions.ObjectsNotExist(f"User <{user_id}> 不存在")

    def assert_post_id_is_not_none(self):
        if self.id is None:
            raise exceptions.ArgumentInvalid("post_id 不能为 None")

    def get_post(self):
        self.assert_post_id_is_not_none()

        post = self.get_sqlalchemy_instance()
        condition = and_(Comment.deleted == False, Comment.post_id == self.id)
        comments_count = Comment.query.filter(condition).count()

        return ResponsePostModel(comments_count=comments_count, **post.as_dict())

    def get_posts(self, **kwargs):
        self.assert_topic_id_is_not_none()
        per_page = kwargs["per_page"]
        offset = kwargs["offset"]

        condition = and_(Post.deleted == False, Post.topic_id == self.topic_id)
        posts = self._model.query.filter(condition).offset(offset).limit(per_page)
        yield from (ResponsePostModel(comments_count=0, **instance.as_dict()) for instance in posts)

    def create_post(self, **kwargs):
        self.assert_topic_id_is_not_none()
        self.assert_topic_exist()

        user_id = kwargs["user_id"]
        self.assert_user_exist(user_id)

        content = kwargs["content"]
        if content is None or len(content.strip()) <= POST_MINIMUM_WORDS:
            raise exceptions.ArgumentInvalid(f"Post 文章字数不能少于 <{POST_MINIMUM_WORDS}> 个")

        post = self._model.create(topic_id=self.topic_id, **kwargs)
        return ResponsePostModel(comments_count=-1, **post.as_dict())

    def update_post(self, **kwargs):
        self.assert_topic_id_is_not_none()
        self.assert_topic_exist()

        user_id = kwargs["user_id"]
        self.assert_user_exist(user_id)

        post = self.get_sqlalchemy_instance()
        post.update(**kwargs)

        return self.get_post()

    def delete_post(self):
        instance = self.get_sqlalchemy_instance()
        instance.update(deleted=True)

        return
