from sqlalchemy import JSON, Integer, Text
from sqlalchemy.sql import expression

from models.database import Base, Column, DeleteMixin, TimeMixin


class Post(Base, TimeMixin, DeleteMixin):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, nullable=False, comment="文章所在的主题 ID")
    user_id = Column(Integer, nullable=False, comment="发布文章用户的 ID")
    content = Column(Text, nullable=False, comment="文章内容")
    click_times = Column(Integer, default=0, server_default=expression.false(), comment="文章的点击数")
    tags = Column(JSON, nullable=True, default=[], comment="文章的 tag")
