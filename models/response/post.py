from datetime import datetime
from typing import List, Optional

from pyruicore import BaseModel


class ResponsePostModel(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    topic_id: Optional[int]
    content: str
    comments_count: Optional[int]
    click_times: Optional[int]
    tags: Optional[List[str]]
    create_time: datetime
    update_time: datetime
