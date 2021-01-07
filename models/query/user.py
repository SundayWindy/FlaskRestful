from typing import Optional

from pyruicore import Field

from models.query import BaseQueryModel


class UserQueryModel(BaseQueryModel):
    email: Optional[str] = Field(location="json")
    password: Optional[str] = Field(location="json", comment="登陆密码 hash 之后的值")
    name: Optional[str] = Field(location="json", default="this is name")
    phone: Optional[str] = Field(location="json")
    avatar: Optional[str] = Field(location="json")
    website: Optional[str] = Field(location="json")
    company: Optional[str] = Field(location="json")
    job: Optional[str] = Field(location="json")
