from models.base_model import Field
from models.data_types import IntType, StringType
from models.response_models.base_model import BaseResponseModel


class TopicResponseModel(BaseResponseModel):
    id = Field(IntType(), nullable=False)
    name = Field(StringType(), nullable=False, comment="主题名称")
