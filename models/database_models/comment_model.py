from sqlalchemy import Integer, Text, DateTime, func, Boolean, text

from models.database_models import Base, Column


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, )
    user_id = Column(Integer, nullable=False, comment="评论用户的 ID")
    post_id = Column(Integer, nullable=False, comment="Post 文章的 ID")
    content = Column(Text, nullable=False, comment="用户的评论")

    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    deleted = Column(Boolean, default=False, server_default=text('0'), nullable=False, comment="该项目是否被删除")
