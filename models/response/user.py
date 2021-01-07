from datetime import datetime
from typing import Optional

from pyruicore import BaseModel


class ResponseUserModel(BaseModel):
    id: Optional[int]
    email: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    avatar: Optional[str]
    website: Optional[str]
    company: Optional[str]
    job: Optional[str]
    create_time: Optional[datetime]
    update_time: Optional[datetime]
