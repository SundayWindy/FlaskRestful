from models.data_types import *
from models.query_model import BaseQueryModel, QueryField


class UserQueryModel(BaseQueryModel):
    email = QueryField(StringType(), nullable=True, location="json")
    password = QueryField(StringType(), nullable=True, location="json", comment="登陆密码 hash 之后的值")

    name = QueryField(StringType(), required=False, location="json")
    phone = QueryField(StringType(), required=False, location="json")  # 改电话号码需要验证
    avatar = QueryField(StringType(), required=False, location="json")
    website = QueryField(StringType(), required=False, location="json")
    company = QueryField(StringType(), required=False, location="json")
    job = QueryField(StringType(), required=False, location="json")
    location = QueryField(StringType(), required=False, location="json")
    signature = QueryField(StringType(), required=False, location="json")
    Dribbble = QueryField(StringType(), required=False, location="json")
    Duolingo = QueryField(StringType(), required=False, location="json")
    About_me = QueryField(StringType(), required=False, location="json")
    Last_me = QueryField(StringType(), required=False, location="json")
    Goodreads = QueryField(StringType(), required=False, location="json")
    GitHub = QueryField(StringType(), required=False, location="json")
    PSN_ID = QueryField(StringType(), required=False, location="json")
    Steam_ID = QueryField(StringType(), required=False, location="json")
    Twitch = QueryField(StringType(), required=False, location="json")
    BattleTag = QueryField(StringType(), required=False, location="json")
    Instagram = QueryField(StringType(), required=False, location="json")
    Telegram = QueryField(StringType(), required=False, location="json")
    Twitter = QueryField(StringType(), required=False, location="json")
    BTC_Address = QueryField(StringType(), required=False, location="json")
    Coding_net = QueryField(StringType(), required=False, location="json")
    Personal_Introduction = QueryField(StringType(), required=False, location="json")
    state_update_view_permission = QueryField(IntType(), required=False, location="json")
    community_rich_rank = QueryField(BooleanType(), required=False, location="json")
    money = QueryField(IntType(), required=False, location="json")
    show_remain_money = QueryField(BooleanType(), required=False, location="json")
    use_avatar_for_favicon = QueryField(BooleanType(), required=False, location="json")
    use_high_resolution_avatar = QueryField(BooleanType(), required=False, location="json")
    time_zone = QueryField(StringType(), required=False, location="json")
