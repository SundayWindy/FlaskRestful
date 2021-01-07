from sqlalchemy import Integer, Text

from models.orm import Base, Column, DeleteMixin, TimeMixin


class Comment(Base, TimeMixin, DeleteMixin):
    __tablename__ = "comment"

    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)
    content = Column(Text, nullable=False, comment="user's comment content")
