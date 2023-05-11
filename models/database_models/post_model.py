from sqlalchemy import JSON, Boolean, DateTime, Integer, Text, func, text

from models.database_models.base_model import Base, Column


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, nullable=False, comment='文章所在的主题 ID')
    user_id = Column(Integer, nullable=False, comment='发布文章用户的 ID')
    content = Column(Text, nullable=False, comment='')
    click_times = Column(Integer, default=0, server_default=text('0'), comment='文章的点击数')
    tags = Column(JSON, nullable=True, default=[], comment='文章的 tag')

    create_time = Column(DateTime, server_default=func.now(), comment='创建时间')
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')
    deleted = Column(
        Boolean,
        default=False,
        server_default=text('0'),
        nullable=False,
        comment='该项目是否被删除',
    )
