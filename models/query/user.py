from models.data_types import StringType
from models.query import BaseQueryModel, QueryField


class UserQueryModel(BaseQueryModel):
    email = QueryField(StringType(), location="json")
    password = QueryField(StringType(), location="json", comment="登陆密码 hash 之后的值")

    name = QueryField(StringType(), location="json")
    phone = QueryField(StringType(), location="json")
    avatar = QueryField(StringType(), location="json")
    website = QueryField(StringType(), location="json")
    company = QueryField(StringType(), location="json")
    job = QueryField(StringType(), location="json")
