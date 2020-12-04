from models.data_types import StringType
from models.query import BaseQueryModel, QueryField


class TopicQueryModel(BaseQueryModel):
    name = QueryField(StringType(), location="json", comment="主题名")


class RootTopicQueryModel(TopicQueryModel):
    pass
