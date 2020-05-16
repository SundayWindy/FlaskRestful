from models.base_model import Field
from models.data_types import DateTimeType, IntType, ListType, StringType
from models.response_models.base_model import BaseResponseModel


class ResponsePostModel(BaseResponseModel):
    id = Field(IntType(), nullable=False)
    user_id = Field(IntType(), nullable=False)
    topic_id = Field(IntType(), nullable=False)
    content = Field(StringType(), nullable=False)

    comments_count = Field(IntType(), nullable=False)
    click_times = Field(IntType(), nullable=False)
    tags = Field(ListType(StringType()), nullable=True)

    create_time = Field(DateTimeType(), nullable=False)
    update_time = Field(DateTimeType(), nullable=False)


