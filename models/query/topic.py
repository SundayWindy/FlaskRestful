from typing import Optional

from pyruicore import Field

from models.query import BaseQueryModel


class TopicQueryModel(BaseQueryModel):
    name: Optional[str] = Field(location="json", comment="主题名")


class RootTopicQueryModel(TopicQueryModel):
    pass
