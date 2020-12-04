from models.base import Field
from models.data_types import DateTimeType, IntType, StringType
from models.response import BaseResponseModel


class ResponseUserModel(BaseResponseModel):
    id = Field(IntType(), nullable=False)
    email = Field(StringType(), nullable=False)

    name = Field(StringType())
    phone = Field(StringType(), comment='电话号码')
    avatar = Field(StringType(), comment="用户头像")
    website = Field(StringType(), comment="个人网站")
    company = Field(StringType(), comment="所在公司")
    job = Field(StringType(), comment="职位")

    create_time = Field(DateTimeType(), nullable=False)
    update_time = Field(DateTimeType(), nullable=False)
