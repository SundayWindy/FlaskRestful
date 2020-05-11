from configures import BaseEnumType

BLANK = ""

DATE_FORMATS = ['%Y-%m-%dT%H:%M:%S',
                '%Y-%m-%dT%H:%M:%S.%f',
                '%Y-%m-%d %H:%M:%S.%f',
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%d',
                '%H:%M:%S']


class StateUpdateViewPermission(BaseEnumType):
    # 状态更新查看权限
    All = 0
    LoggedInUser = 1
    Own = 2
