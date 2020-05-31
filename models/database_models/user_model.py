from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import Boolean, DateTime, Integer, String, func, text
from werkzeug.security import check_password_hash, generate_password_hash

from configures import settings
from models.database_models.base_model import Base, Column


class User(Base):
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
    location = Column(String(100), nullable=True, comment="所在地")
    signature = Column(String(256), nullable=True, comment="签名")
    Dribbble = Column(String(256), nullable=True, comment="Dribbble")
    Duolingo = Column(String(256), nullable=True, comment="Duolingo")
    About_me = Column(String(256), nullable=True, comment="About.me")
    Last_me = Column(String(256), nullable=True, comment="Last.fm")
    Goodreads = Column(String(256), nullable=True, comment="Goodreads")
    GitHub = Column(String(256), nullable=True, comment="GitHub")
    PSN_ID = Column(String(256), nullable=True, comment="PSN ID")
    Steam_ID = Column(String(256), nullable=True, comment="Steam_ID")
    Twitch = Column(String(256), nullable=True, comment="Twitch")
    BattleTag = Column(String(256), nullable=True, comment="BattleTag")
    Instagram = Column(String(256), nullable=True, comment="Instagram")
    Telegram = Column(String(256), nullable=True, comment="Telegram")
    Twitter = Column(String(256), nullable=True, comment="Twitter")
    BTC_Address = Column(String(256), nullable=True, comment="BTC Address")
    Coding_net = Column(String(256), nullable=True, comment="Coding.net")
    Personal_Introduction = Column(String(256), nullable=True, comment="个人简介")
    state_update_view_permission = Column(Integer, default=0, comment="状态更新查看权限")
    community_rich_rank = Column(Boolean, default=False, comment="社区财富排行榜")
    money = Column(Integer, default=0, comment="余额")
    show_remain_money = Column(Boolean, default=0, comment="是否显示余额")
    use_avatar_for_favicon = Column(Boolean, default=0, comment="使用节点头像作为页面 favicon")
    use_high_resolution_avatar = Column(Boolean, default=0, comment="使用高精度头像")
    time_zone = Column(String(256), default="utc", comment="默认使用的时区")

    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    deleted = Column(
        Boolean, default=False, server_default=text('0'), nullable=False, comment="该项目是否被删除"
    )

    def __repr__(self):
        return f"User<{self.name}>"

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=600):
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
