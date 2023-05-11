from models.base_model import Field
from models.data_types import ApiDefineType, IntType, ListType, StringType
from models.response_models.base_model import BaseResponseModel


class TopicResponseModel(BaseResponseModel):
    id = Field(IntType(), nullable=False)
    name = Field(StringType(), nullable=False, comment='主题名称')
    posts_count = Field(IntType(), nullable=True, comment='评论总数')


class RootTopicResponseModel(BaseResponseModel):
    id = Field(IntType(), nullable=False)
    name = Field(StringType(), nullable=False, comment='主题名称')

    child_topics = Field(
        ListType(ApiDefineType(TopicResponseModel)),
        nullable=False,
        mock_func=lambda: [],
        comment='根topic下的所有子topic',
    )
