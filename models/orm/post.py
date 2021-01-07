from sqlalchemy import JSON, Integer, Text
from sqlalchemy.sql import expression

from models.orm import Base, Column, DeleteMixin, TimeMixin


class Post(Base, TimeMixin, DeleteMixin):
    __tablename__ = "post"

    content = Column(Text, nullable=False)
    user_id = Column(Integer, nullable=False)
    topic_id = Column(Integer, nullable=False)
    tags = Column(JSON, nullable=True, default=[])
    click_times = Column(Integer, default=0, server_default=expression.false())
