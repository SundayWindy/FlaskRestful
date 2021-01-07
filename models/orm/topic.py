from sqlalchemy import ForeignKey, Integer, String, text

from models.orm import Base, Column, DeleteMixin, TimeMixin


class RootTopic(Base, TimeMixin, DeleteMixin):
    __tablename__ = "root_topic"

    name = Column(String(256), nullable=False, unique=True)


class Topic(Base, TimeMixin, DeleteMixin):
    __tablename__ = "topic"

    name = Column(String(256), nullable=False, unique=True)
    root_topic_id = Column(Integer, ForeignKey("root_topic.id"), server_default=text("1"))
