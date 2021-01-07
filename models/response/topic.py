from typing import List, Optional

from pyruicore import BaseModel, Field


class TopicResponseModel(BaseModel):
    id: Optional[int]
    name: Optional[str] = Field(comment="主题名称")
    posts_count: Optional[int] = Field(comment="评论总数")


class RootTopicResponseModel(BaseModel):
    id: Optional[int]
    name: Optional[str] = Field(comment="主题名称")
    child_topics: Optional[List[TopicResponseModel]] = Field(
        nullable=False,
        default_factory=lambda: [],
        comment="根topic下的所有子topic",
    )
