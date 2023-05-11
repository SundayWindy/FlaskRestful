from itertools import groupby
from typing import Generator, List, Optional, TypeVar

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

from exceptions.exceptions import ActionNotAllowed, ObjectsDuplicated
from handlers import BaseHandler
from handlers.utils import assert_name_is_valid
from models.database_models import RootTopic, Topic
from models.response_models.topic_model import RootTopicResponseModel, TopicResponseModel

SqlAlchemyModel = TypeVar('SqlAlchemyModel', bound=SQLAlchemy)


class RootTopicHandler(BaseHandler):
    _model = RootTopic

    def __init__(self, id: int = None) -> None:
        super().__init__(id)
        self.error_msg = f'Root Topic <{id}> 不存在'

    def get_topic(self) -> Generator[RootTopicResponseModel, None, None]:
        instance = self._get_sqlalchemy_instance()

        condition = and_(Topic.deleted == False, Topic.root_topic_id == self.id)
        child_topics = (TopicResponseModel(**topic.as_dict()) for topic in Topic.query.filter(condition))

        yield RootTopicResponseModel(child_topics=child_topics, **instance.as_dict())

    @staticmethod
    def sort_and_group_child_topic(
        root_topic_ids,
    ) -> Generator[List[SqlAlchemyModel], None, None]:
        child_topics = Topic.query.filter_by(deleted=False).filter(Topic.root_topic_id.in_(root_topic_ids))
        child_topics = sorted(child_topics, key=lambda x: x.root_topic_id)

        groups = {k: list(v) for k, v in groupby(child_topics, key=lambda x: x.root_topic_id)}
        yield from map(lambda k: groups.get(k, []), root_topic_ids)

    def get_topics(self) -> Generator[RootTopicResponseModel, None, None]:
        root_topics = self._model.query.filter_by(deleted=False)
        root_topic_ids = [ins.id for ins in root_topics]
        child_topics = self.sort_and_group_child_topic(root_topic_ids)

        for root_topic, topic in zip(root_topics, child_topics):
            ch_topics = (TopicResponseModel(**t.as_dict()) for t in topic)
            yield RootTopicResponseModel(child_topics=ch_topics, **root_topic.as_dict())

    def create_topic(self, **kwargs) -> Generator[RootTopicResponseModel, None, None]:
        assert_name_is_valid(message='根主题名不能为空', **kwargs)

        name = kwargs['name']
        condition = and_(self._model.deleted == False, self._model.name == name)
        instance = self._model.query.filter(condition).first()
        if instance:
            raise ObjectsDuplicated(f'名称为 <{name}> 的根 Topic 已经创建')

        instance = self._model.create(**kwargs)
        yield RootTopicResponseModel(child_topics=[], **instance.as_dict())

    def update_topic(self, **kwargs) -> Generator[RootTopicResponseModel, None, None]:
        assert_name_is_valid(message='主题名不能为空', **kwargs)
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

        yield RootTopicResponseModel(child_topics=[], **instance.as_dict())

    def delete_topic(self) -> None:
        raise ActionNotAllowed('根主题不允许被删除')
