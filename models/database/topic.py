from sqlalchemy import ForeignKey, Integer, String, text

from models.database import Base, Column, DeleteMixin, TimeMixin


class RootTopic(Base, TimeMixin, DeleteMixin):
    __tablename__ = "root_topic"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)


class Topic(Base, TimeMixin, DeleteMixin):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)
    root_topic_id = Column(Integer, ForeignKey("root_topic.id"), server_default=text('1'))


if __name__ == '__main__':
    from app import create_app

    app = create_app()
    app.app_context().push()
    RootTopic.create(name="root_topic")
