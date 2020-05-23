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

    ALLOWED_PATTERN = r'^[\S]+$'
    ERROR_MSG = '不允许出现空白字符'

    @classmethod
    def is_allowed(cls, value: str) -> bool:
        pattern = re.compile(cls.ALLOWED_PATTERN)
        is_match = re.search(pattern, value)
        return True if is_match else False

    @classmethod
    def check(cls, value: str):
        if not cls.is_allowed(value):
            raise exceptions.PatternInvalid(cls.ERROR_MSG)
        return value


class EmailChecker(BaseChecker):
    ALLOWED_PATTERN = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    ERROR_MSG = '邮箱格式错误'


class PassWordChecker(BaseChecker):
    ALLOWED_PATTERN = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*#?&]{8,}"
    ERROR_MSG = "密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符,不能含有空格"


class NameChecker(BaseChecker):
    ALLOWED_PATTERN = '^[\\w\u4e00-\u9fa5-]+$'
    ERROR_MSG = '名称中只允许出现【中文，英文，数字，下划线，连接符】,并且不允许全部是空白字符'


class ContentChecker(BaseChecker):
    ALLOWED_PATTERN = r'[\S]+'
    ERROR_MSG = '不允许全部是空白字符，即至少有一个非空白字符'


def assert_name_is_valid(message="名称不能为空", **kwargs) -> None:
    # 检查传入的参数中，name 字段是否为空
    name = kwargs.get("name")
    if name is None:
        raise exceptions.ArgumentRequired(message)
    if not NameChecker.is_allowed(name):
        raise exceptions.ArgumentInvalid(NameChecker.ERROR_MSG)
