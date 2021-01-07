from typing import Optional

from itsdangerous import (
    BadSignature,
    SignatureExpired,
    TimedJSONWebSignatureSerializer as Serializer,
)
from sqlalchemy import String
from werkzeug.security import check_password_hash, generate_password_hash

from configures import settings
from models.orm import Base, Column, DeleteMixin, TimeMixin


class User(Base, TimeMixin, DeleteMixin):
    __tablename__ = "user"

    email = Column(String(100), nullable=False)
    password_hash = Column(String(256), nullable=False)
    job = Column(String(100), nullable=True)
    name = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    avatar = Column(String(256), nullable=True)
    website = Column(String(100), nullable=True)
    company = Column(String(100), nullable=True)

    def hash_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=3600) -> bool:
        return Serializer(settings.SECRET_KEY, expires_in=expiration).dumps({"id": self.id})

    @staticmethod
    def verify_auth_token(token: str) -> Optional["User"]:
        s = Serializer(settings.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data["id"])
        return user

    def __repr__(self):
        return f"User<{self.name}>"
