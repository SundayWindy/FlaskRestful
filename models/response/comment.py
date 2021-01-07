from datetime import datetime

from pyruicore import BaseModel


class ResponseCommentModel(BaseModel):
    id: int
    user_id: int
    post_id: int
    content: str
    create_time: datetime
    update_time: datetime
