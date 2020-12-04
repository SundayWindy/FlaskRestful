from models.base import Field
from models.data_types import DateTimeType, IntType, StringType
from models.response import BaseResponseModel


class ResponseCommentModel(BaseResponseModel):
    id = Field(IntType(), nullable=False)
    user_id = Field(IntType(), nullable=False)
    post_id = Field(IntType(), nullable=False)
    content = Field(StringType(), nullable=False)

    create_time = Field(DateTimeType(), nullable=False)
    update_time = Field(DateTimeType(), nullable=False)
