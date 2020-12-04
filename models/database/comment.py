from sqlalchemy import Integer, Text

from models.database import Base, Column, DeleteMixin, TimeMixin


class Comment(Base, TimeMixin, DeleteMixin):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True,)
    user_id = Column(Integer, nullable=False, comment="评论用户的 ID")
    post_id = Column(Integer, nullable=False, comment="Post 文章的 ID")
    content = Column(Text, nullable=False, comment="用户的评论")
