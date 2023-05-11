from models.base_model import Field
from models.data_types import BooleanType, DateTimeType, IntType, StringType
from models.response_models.base_model import BaseResponseModel


class ResponseUserModel(BaseResponseModel):
    id = Field(IntType(), nullable=False)
    email = Field(StringType(), nullable=False)

    name = Field(StringType(), nullable=True)
    phone = Field(StringType(), nullable=True, comment='电话号码')
    avatar = Field(StringType(), nullable=True, comment='用户头像')
    website = Field(StringType(), nullable=True, comment='个人网站')
    company = Field(StringType(), nullable=True, comment='所在公司')
    job = Field(StringType(), nullable=True, comment='职位')
    location = Field(StringType(), nullable=True, comment='所在地')
    signature = Field(StringType(), nullable=True, comment='签名')
    Dribbble = Field(StringType(), nullable=True, comment='Dribbble')
    Duolingo = Field(StringType(), nullable=True, comment='Duolingo')
    About_me = Field(StringType(), nullable=True, comment='About.me')
    Last_me = Field(StringType(), nullable=True, comment='Last.fm')
    Goodreads = Field(StringType(), nullable=True, comment='Goodreads')
    GitHub = Field(StringType(), nullable=True, comment='GitHub')
    PSN_ID = Field(StringType(), nullable=True, comment='PSN ID')
    Steam_ID = Field(StringType(), nullable=True, comment='Steam_ID')
    Twitch = Field(StringType(), nullable=True, comment='Twitch')
    BattleTag = Field(StringType(), nullable=True, comment='BattleTag')
    Instagram = Field(StringType(), nullable=True, comment='Instagram')
    Telegram = Field(StringType(), nullable=True, comment='Telegram')
    Twitter = Field(StringType(), nullable=True, comment='Twitter')
    BTC_Address = Field(StringType(), nullable=True, comment='BTC Address')
    Coding_net = Field(StringType(), nullable=True, comment='Coding.net')
    Personal_Introduction = Field(StringType(), nullable=True, comment='个人简介')
    state_update_view_permission = Field(IntType(), comment='状态更新查看权限')
    community_rich_rank = Field(BooleanType(), comment='社区财富排行榜')
    money = Field(IntType(), comment='余额')
    show_remain_money = Field(BooleanType(), comment='是否显示余额')
    use_avatar_for_favicon = Field(BooleanType(), comment='使用节点头像作为页面 favicon')
    use_high_resolution_avatar = Field(BooleanType(), comment='使用高精度头像')
    time_zone = Field(StringType(), comment='默认使用的时区')

    create_time = Field(DateTimeType(), nullable=False)
    update_time = Field(DateTimeType(), nullable=False)
