from configures import BaseEnumType

PER_PAGE = 50
POST_MINIMUM_WORDS = 5
BLANK = ""

DATE_FORMATS = [
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M:%S.%f",
    "%Y-%m-%d %H:%M:%S.%f",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",
    "%H:%M:%S",
]


class StateUpdateViewPermission(BaseEnumType):
    # 状态更新查看权限
    All = 0
    LoggedInUser = 1
    Own = 2
