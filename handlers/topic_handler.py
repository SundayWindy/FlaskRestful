from typing import Generator, Optional

from sqlalchemy import and_

from exceptions.exceptions import ObjectsDuplicated
from handlers import BaseHandler
from handlers.utils import assert_name_is_valid
from models.database_models.post_model import Post
from models.database_models.topic_model import Topic
from models.response_models.topic_model import TopicResponseModel


class TopicHandler(BaseHandler):
    _model = Topic

    def __init__(self, id: int = None) -> None:
        super().__init__(id)
        self.error_msg = f'Topic <{id}> 不存在'

    @staticmethod
    def get_post_count(instance: Post) -> int:
        condition = and_(Post.deleted == False, Post.topic_id == instance.id)
        total = Post.query.filter(condition).count()
        return total

    def get_topic(self) -> TopicResponseModel:
        instance = self._get_sqlalchemy_instance()
        total = self.get_post_count(instance)

        return TopicResponseModel(posts_count=total, **instance.as_dict())

    def get_topics(self) -> Generator[TopicResponseModel, None, None]:
        instances = self._model.query.filter_by(deleted=False)
        for instance in instances:
            total = self.get_post_count(instance)
            yield TopicResponseModel(posts_count=total, **instance.as_dict())

    def create_topic(self, **kwargs) -> TopicResponseModel:
        assert_name_is_valid(message='主题名不能为空', **kwargs)
        name = kwargs['name']
        condition = and_(self._model.deleted == False, self._model.name == name)
        instance = self._model.query.filter(condition).first()
        if instance:
            raise ObjectsDuplicated(f'名称为 <{name}> 的 Topic 已经创建')
        instance = self._model.create(**kwargs)

        return TopicResponseModel(posts_count=0, **instance.as_dict())

    def update_topic(self, **kwargs) -> Optional[TopicResponseModel]:
        assert_name_is_valid(message='主题名不能为空', **kwargs)
        self.assert_id_is_not_none()

        name = kwargs['name']
        condition = and_(
            self._model.deleted == False,
            self._model.id != self.id,
            self._model.name == name,
        )
        instance = self._model.query.filter(condition).first()
        if instance:
            raise ObjectsDuplicated(f'名称为 <{name}> 的 Topic 已经创建')

        instance = self._get_sqlalchemy_instance()
        instance.update(name=name)
        total = self.get_post_count(instance)

        return TopicResponseModel(posts_count=total, **instance.as_dict())

    def delete_topic(self) -> None:
        instance = self._get_sqlalchemy_instance()
        instance.update(deleted=True)

        return
