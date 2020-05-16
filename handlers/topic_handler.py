from exceptions import exceptions

from sqlalchemy import and_

from configures.help_funcs import BasicNameChecker
from handlers import BaseHandler
from models.database_models.topic_model import Topic
from models.response_models.topic_model import TopicResponseModel


class TopicHandler(BaseHandler):
    _model = Topic

    def __init__(self, id=None):
        super().__init__(id)
        self.error_msg = f"Topic <{id}> 不存在"

    @staticmethod
    def assert_name_is_not_none(**kwargs) -> None:
        # 检查传入的参数中，name 字段是否为空
        name = kwargs.get("name")
        if name is None:
            raise exceptions.ArgumentRequired("主题名不能为空")
        if not BasicNameChecker.is_allowed(name):
            raise exceptions.ArgumentInvalid(BasicNameChecker.ERROR_MSG)

    def get_topic(self) -> TopicResponseModel:
        instance = self.get_sqlalchemy_instance()

        return TopicResponseModel(**instance.as_dict())

    def get_topics(self):
        instances = self._model.query.filter_by(deleted=False)
        yield from (TopicResponseModel(**ins.as_dict()) for ins in instances)

    def create_topic(self, **kwargs) -> TopicResponseModel:
        self.assert_name_is_not_none(**kwargs)

        name = kwargs["name"]
        condition = and_(self._model.deleted == False, self._model.name == name)
        instance = self._model.query.filter(condition).first()
        if instance:
            raise exceptions.ObjectsDuplicated(f"名称为 <{name}> 的 Topic 已经创建")

        instance = self._model.create(**kwargs)

        return TopicResponseModel(**instance.as_dict())

    def update_topic(self, **kwargs) -> TopicResponseModel:

        self.assert_name_is_not_none(**kwargs)
        self.assert_id_is_not_none()

        name = kwargs["name"]
        condition = and_(
            self._model.deleted == False, self._model.id != self.id, self._model.name == name
        )
        instance = self._model.query.filter(condition).first()

        if instance:
            raise exceptions.ObjectsDuplicated(f"名称为 <{name}> 的 Topic 已经创建")

        instance = self.get_sqlalchemy_instance()
        instance.update(name=name)

        return TopicResponseModel(**instance.as_dict())

    def delete_topic(self) -> None:
        instance = self.get_sqlalchemy_instance()
        instance.update(deleted=True)

        return
