from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import Integer, String
from werkzeug.security import check_password_hash, generate_password_hash

from configures import settings
from models.database import Base, Column, DeleteMixin, TimeMixin


class User(Base, TimeMixin, DeleteMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    email = Column(String(100), nullable=False)
    password_hash = Column(String(256), nullable=False, comment="登陆密码 hash 之后的值")

    name = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True, comment='电话号码')
    avatar = Column(String(256), nullable=True, comment="用户头像")
    website = Column(String(100), nullable=True, comment="个人网站")
    company = Column(String(100), nullable=True, comment="所在公司")
    job = Column(String(100), nullable=True, comment="职位")

    def __repr__(self):
        return f"User<{self.name}>"

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=3600):
        s = Serializer(settings.SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(settings.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


if __name__ == '__main__':
    s = Serializer(settings.SECRET_KEY)
    token = (
        "eyJhbGciOiJIUzUxMiIsImlhdCI"
        "6MTYwNzA3NjE0MCwiZXhwIjoxNjA3MDc2Nz"
        "QwfQ.eyJpZCI6MX0.9FwLXUqnm993TFxMbm98pXVCUoCV"
        "J491Qcz5OsDxCW7-dJWRd1M3oTVUD3uVfveNoOGjF0cbi2r6YnBPf7Qyfw"
    )
    m = s.loads(token)
    print(m)
