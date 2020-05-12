import random
from uuid import uuid1
from datetime import datetime
from collections.abc import Iterable
from models import ApiDataType
from configures.help_funcs import str_to_datetime


class IntType(ApiDataType):
    def mock(self):
        return random.randint(0, 10)

    def marshal(self, value):
        return int(value) if value is not None and value != "" else None

    def validate(self, value):
        assert value is None or isinstance(value, int)


class FloatType(ApiDataType):
    def mock(self):
        return int(random.random() * 100) / 10

    def marshal(self, value):
        return float(value) if value is not None and value != "" else None

    def validate(self, value):
        assert value is None or isinstance(value, float)


class StringType(ApiDataType):
    def mock(self):
        return uuid1().hex

    def marshal(self, value):
        return str(value) if value not in (None, "") else None

    def validate(self, value):
        assert value is None or isinstance(value, str)


class BooleanType(ApiDataType):
    def mock(self):
        return random.choice([True, False])

    def marshal(self, value):
        if value == "":
            value = None
        if isinstance(value, str):
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
        assert (value in (True, False, None)), "[Boolean] should be [True] or [False]. Actual: [{}]".format(type(value))

        return value

    def validate(self, value):
        assert value is None or isinstance(value, bool)


class DateTimeType(ApiDataType):
    def mock(self):
        return datetime.fromtimestamp(1000000000 * random.random())

    def marshal(self, value):
        date = None
        if value and value not in ("", "null", "None"):
            if isinstance(value, datetime):
                date = value
            elif isinstance(value, str):
                date = str_to_datetime(value)
            else:
                raise TypeError("Invalid datetime format")

        return date

    def validate(self, value):
        assert value is None or isinstance(value, datetime)


class ListType(ApiDataType):
    def __init__(self, element_type: ApiDataType):
        self.element_type = element_type

    def mock(self):
        return [self.element_type.mock() for _ in range(10)]

    def marshal(self, value):
        return [] if not value else [self.element_type.marshal(v) for v in value]

    def validate(self, value):
        assert isinstance(value, Iterable) and not isinstance(value, str)
        for v in value:
            self.element_type.validate(v)

    def __str__(self):
        return "List<{}>".format(self.element_type)


class DictType(ApiDataType):

    def mock(self):
        return {uuid1().hex: uuid1().hex}

    def marshal(self, value):
        return value

    def validate(self, value):
        assert isinstance(value, dict)
