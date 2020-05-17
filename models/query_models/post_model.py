from models.data_types import IntType, StringType
from models.query_models.base_model import BaseQueryModel, QueryField

from configures.const import PER_PAGE


class PostQueryModel(BaseQueryModel):
    user_id = QueryField(IntType(), nullable=True, location="json")
    content = QueryField(StringType(), nullable=True, location="json")

    per_page = QueryField(IntType(), default=PER_PAGE, location="json")
    offset = QueryField(IntType(), default=0, location="json")
