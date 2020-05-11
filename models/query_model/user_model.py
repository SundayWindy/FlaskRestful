from models.data_types import *
from models.query_model import BaseQueryModel, QueryField


class UserQueryModel(BaseQueryModel):
    email = QueryField(StringType(), nullable=True)
    password = QueryField(StringType, nullable=True, comment="登陆密码 hash 之后的值")

    name = QueryField(StringType(), required=False)
    phone = QueryField(StringType(), required=False)  # 改电话号码需要验证
    avatar = QueryField(StringType(), required=False)
    website = QueryField(StringType(), required=False)
    company = QueryField(StringType(), required=False)
    job = QueryField(StringType(), required=False)
    location = QueryField(StringType(), required=False)
    signature = QueryField(StringType(), required=False)
    Dribbble = QueryField(StringType(), required=False)
    Duolingo = QueryField(StringType(), required=False)
    About_me = QueryField(StringType(), required=False)
    Last_me = QueryField(StringType(), required=False)
    Goodreads = QueryField(StringType(), required=False)
    GitHub = QueryField(StringType(), required=False)
    PSN_ID = QueryField(StringType(), required=False)
    Steam_ID = QueryField(StringType(), required=False)
    Twitch = QueryField(StringType(), required=False)
    BattleTag = QueryField(StringType(), required=False)
    Instagram = QueryField(StringType(), required=False)
    Telegram = QueryField(StringType(), required=False)
    Twitter = QueryField(StringType(), required=False)
    BTC_Address = QueryField(StringType(), required=False)
    Coding_net = QueryField(StringType(), required=False)
    Personal_Introduction = QueryField(StringType(), required=False)
    state_update_view_permission = QueryField(IntType(), required=False)
    community_rich_rank = QueryField(BooleanType(), required=False)
    money = QueryField(IntType(), required=False)
    show_remain_money = QueryField(BooleanType(), required=False)
    use_avatar_for_favicon = QueryField(BooleanType(), crequired=False)
    use_high_resolution_avatar = QueryField(BooleanType(), required=False)
    time_zone = QueryField(StringType(), required=False)
