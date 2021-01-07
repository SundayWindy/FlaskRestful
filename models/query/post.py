from typing import Optional

from pyruicore import Field

from configures.const import PER_PAGE
from models.query import BaseQueryModel


class PostQueryModel(BaseQueryModel):
    user_id: Optional[int] = Field(location="json")
    content: Optional[str] = Field(location="json")
    per_page: Optional[int] = Field(default=PER_PAGE, location="json")
    offset: Optional[int] = Field(default=0, location="json")
