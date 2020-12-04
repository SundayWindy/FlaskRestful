import importlib
import random
from collections.abc import Iterable
from datetime import datetime
from exceptions.exceptions import ServerException
from typing import Any, Callable, Dict, List, Optional, Tuple, Type
from uuid import uuid1

from handlers.utils import str_to_datetime
from models.base import ApiDataType, BaseModel


class IntType(ApiDataType):
    def mock(self) -> int:
        return random.randint(0, 10)

    def marshal(self, value) -> Optional[int]:
        return int(value) if value is not None and value != "" else None

    def validate(self, value) -> None:
        assert value is None or isinstance(value, int)


class FloatType(ApiDataType):
    def mock(self) -> float:
        return int(random.random() * 100) / 10

    def marshal(self, value) -> Optional[float]:
        return float(value) if value is not None and value != "" else None

    def validate(self, value) -> None:
        assert value is None or isinstance(value, float)


class StringType(ApiDataType):
    def mock(self) -> str:
        return uuid1().hex

    def marshal(self, value) -> Optional[str]:
        if self.implicit:
            return str(value) if value not in (None, "") else None
        else:
            self.validate(value)
            return value

    def validate(self, value) -> None:
        assert value is None or isinstance(
            value, str
        ), f"expect  <class 'str'>, but get {type(value)}"


class BooleanType(ApiDataType):
    def mock(self) -> bool:
        return random.choice([True, False])

    def marshal(self, value) -> bool:
        if value == "":
            value = None
        if isinstance(value, str):
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
        assert value in (
            True,
            False,
            None,
        ), "[Boolean] should be [True] or [False]. Actual: [{}]".format(type(value))

        return value

    def validate(self, value) -> None:
        assert value is None or isinstance(value, bool)


class DateTimeType(ApiDataType):
    def mock(self) -> datetime:
        return datetime.fromtimestamp(1000000000 * random.random())

    def marshal(self, value) -> Optional[datetime]:
        date = None
        if value and value not in ("", "null", "None"):
            if isinstance(value, datetime):
                date = value
            elif isinstance(value, str):
                date = str_to_datetime(value)
            else:
                raise TypeError("Invalid datetime format")

        return date

    def validate(self, value) -> None:
        assert value is None or isinstance(value, datetime)


class ListType(ApiDataType):
    def __init__(self, element_type: ApiDataType) -> None:
        self.element_type = element_type

    def mock(self) -> List[Any]:
        return [self.element_type.mock() for _ in range(10)]

    def marshal(self, value) -> List[Any]:
        return [] if not value else [self.element_type.marshal(v) for v in value]

    def validate(self, value) -> None:
        assert isinstance(value, Iterable) and not isinstance(value, str)
        for v in value:
            self.element_type.validate(v)

    def __str__(self):
        return "List<{}>".format(self.element_type)


class DictType(ApiDataType):
    def mock(self) -> Dict[str, str]:
        return {uuid1().hex: uuid1().hex}

    def marshal(self, value) -> Dict[str, str]:
        return value

    def validate(self, value) -> bool:
        assert isinstance(value, dict)


class LazyWrapper:
    def __init__(self, func: Callable = None):
        self._func = func
        self._object = None

    @property
    def object(self) -> Callable:
        if self._object is None:
            self._object = self._func()
        return self._object

    def __getattr__(self, item):
        return getattr(self.object, item)


class ApiDefineType(ApiDataType):
    mod = LazyWrapper(lambda: importlib.import_module("models.response"))

    def __init__(self, schema: Tuple[str, BaseModel]):
        if isinstance(schema, str):
            self.schema_name = schema
            self._real_data_type = None
        elif issubclass(schema, BaseModel):
            self.schema_name = schema.__name__
            self._real_data_type = schema
        else:
            raise ServerException("schema of ApiDefineType should be a Model or name of a Model")

        self._real_data = None

    def _ensure_schema_parsed(self) -> None:
        if self._real_data_type is None:
            self._real_data_type = self._parse_schema_name(self.schema_name)

    @property
    def data_type(self) -> Type[BaseModel]:
        self._ensure_schema_parsed()
        return self._real_data_type

    @classmethod
    def _parse_schema_name(cls, schema_name) -> Optional[BaseModel]:
        schema = getattr(cls.mod, schema_name)
        return schema

    def mock(self):
        raise NotImplementedError()

    def marshal(self, data) -> Dict[Any, Any]:
        self._ensure_schema_parsed()
        if data is None:
            return None
        _data = self.data_type
        return _data.marshal(data)

    def __str__(self):
        return self.schema_name

    def validate(self, data: Any) -> None:
        assert isinstance(data, self.data_type), "Expect: {} - Actual: {}".format(
            self.data_type.__name__, type(data)
        )
        self.marshal(data)
