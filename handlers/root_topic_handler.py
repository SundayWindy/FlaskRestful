from typing import TypeVar, Generator, Tuple, Iterator, Dict, Any, List
from sqlalchemy import and_

from itertools import groupby
from models.database_models import RootTopic, Topic
from models.response_models.topic_model import TopicResponseModel, RootTopicResponseModel, BaseResponseModel

from handlers import BaseHandler
from handlers.utils import assert_name_is_valid

from exceptions.exceptions import ObjectsDuplicated, ActionNotAllowed

ResponseModel = TypeVar("ResponseModel", bound=BaseResponseModel)
SqlAlchemyModel = TypeVar("SqlAlchemyModel")


class RootTopicHandler(BaseHandler):
    _model = RootTopic

    def __init__(self, id=None):
        super().__init__(id)
        self.error_msg = f"Root Topic <{id}> 不存在"

    def get_topic(self) -> ResponseModel:
        instance = self._get_sqlalchemy_instance()

        condition = and_(Topic.deleted == False, Topic.root_topic_id == self.id)
        child_topics = (TopicResponseModel(**topic.as_dict()) for topic in Topic.query.filter(condition))

        return RootTopicResponseModel(child_topics=child_topics, **instance.as_dict())

    @staticmethod
    def sort_and_group_child_topic(root_topic_ids) -> Generator[List[SqlAlchemyModel], None, None]:
        child_topics = Topic.query.filter_by(deleted=False).filter(Topic.root_topic_id.in_(root_topic_ids))
        child_topics = sorted(child_topics, key=lambda x: x.root_topic_id)

        groups = {k: list(v) for k, v in groupby(child_topics, key=lambda x: x.root_topic_id)}
        yield from map(lambda k: groups.get(k, []), root_topic_ids)

    def get_topics(self):
        root_topics = self._model.query.filter_by(deleted=False)
        root_topic_ids = [ins.id for ins in root_topics]
        child_topics = self.sort_and_group_child_topic(root_topic_ids)

        for root_topic, topic in zip(root_topics, child_topics):
            ch_topics = (TopicResponseModel(**t.as_dict()) for t in topic)
            yield RootTopicResponseModel(child_topics=ch_topics, **root_topic.as_dict())

    def create_topic(self, **kwargs) -> ResponseModel:
        assert_name_is_valid(message="根主题名不能为空", **kwargs)

        name = kwargs["name"]
        condition = and_(self._model.deleted == False, self._model.name == name)
        instance = self._model.query.filter(condition).first()
        if instance:
            raise ObjectsDuplicated(f"名称为 <{name}> 的根 Topic 已经创建")

        instance = self._model.create(**kwargs)
        return RootTopicResponseModel(child_topics=[], **instance.as_dict())

    def update_topic(self, **kwargs) -> ResponseModel:
        assert_name_is_valid(message="主题名不能为空", **kwargs)
        name = kwargs["name"]
        condition = and_(
            self._model.deleted == False, self._model.id != self.id, self._model.name == name
        )
        instance = self._model.query.filter(condition).first()
        if instance:
            raise ObjectsDuplicated(f"名称为 <{name}> 的 Topic 已经创建")

        instance = self._get_sqlalchemy_instance()
        instance.update(name=name)

        return RootTopicResponseModel(child_topics=[], **instance.as_dict())

    def delete_topic(self) -> None:
        raise ActionNotAllowed("根主题不允许被删除")
