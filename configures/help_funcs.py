import datetime
import re
from exceptions import exceptions

from configures.const import DATE_FORMATS


def str_to_datetime(value):
    ret = None
    if value and value not in ['', 'null', 'None']:
        for format_ in DATE_FORMATS:
            try:
                ret = datetime.datetime.strptime(value, format_)
                break
            except ValueError:
                pass
        if not ret:
            raise Exception(
                "[date] [time] [datetime] format must be {}, Actual: [{}]".format(
                    DATE_FORMATS, value
                )
            )
    return ret


class BaseChecker:
    # 非空白字符 \S
    # 字母数字下划线 \w  == 【A-Za-z0-9_】
    # 中文 \u4e00-\u9fa5

    ALLOWED_PATTERN = '^[\\S]+$'
    ERROR_MSG = '不允许出现空白字符'

    @classmethod
    def is_allowed(cls, value: str) -> bool:
        pattern = re.compile(cls.ALLOWED_PATTERN)
        is_match = re.search(pattern, value)
        if is_match:
            return True
        return False

    @classmethod
    def check(cls, value: str):
        if not cls.is_allowed(value):
            raise exceptions.InvalidPattern(cls.ERROR_MSG)
        return value


class EmailChecker(BaseChecker):
    ALLOWED_PATTERN = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    ERROR_MSG = '邮箱格式错误'


class PassWordChecker(BaseChecker):
    ALLOWED_PATTERN = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*#?&]{8,}"
    ERROR_MSG = "密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符,不能含有空格"
