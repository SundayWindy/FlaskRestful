from sqlalchemy import Boolean, DateTime, Integer, String, func

from models.database_models.base_model import Base, Column


class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    deleted = Column(Boolean, default=False, comment="该项目是否被删除")
