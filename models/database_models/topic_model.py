from sqlalchemy import Boolean, DateTime, Integer, ForeignKey, String, func, text

from models.database_models.base_model import Base, Column


class RootTopic(Base):
    __tablename__ = "root_topic"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False,unique=True)

    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    deleted = Column(Boolean, default=False, server_default=text('0'), nullable=False, comment="该项目是否被删除")


class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False,unique=True)
    root_topic_id = Column(Integer, ForeignKey("root_topic.id"), server_default=text('1'))

    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    deleted = Column(Boolean, default=False, server_default=text('0'), nullable=False, comment="该项目是否被删除")
