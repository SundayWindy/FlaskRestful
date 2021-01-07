import pprint
from typing import Any, Dict, TypeVar

from flask_restful import reqparse
from pyruicore import BaseModel

from exceptions.exceptions import ArgumentInvalid

T = TypeVar("T", bound=BaseModel)


class BaseQueryModel(BaseModel):
    def __init__(self, **kwargs):
        super(BaseQueryModel, self).__init__(**kwargs)
        self.__storage__ = kwargs
        for field_name in self.__fields_map__.keys():
            if field_name not in self.__storage__:
                delattr(self, field_name)

    @classmethod
    def parse_args(cls) -> T:
        parser = reqparse.RequestParser()

        for field in cls.__fields__:
            name = field.name
            others = field.others
            location = others["location"]
            required = others.get("required", False)
            parser_kwargs = others.get("parser_kwargs", {})
            nullable = field.nullable
            parser.add_argument(
                name, location=location, required=required, nullable=nullable, **parser_kwargs
            )

        parsed = parser.parse_args()

        for field in cls.__fields__:
            if field.enum_values and field.name in parsed:
                value = parsed[field.name]
                if value is not None and value not in field.enum_values:
                    raise ArgumentInvalid(
                        "参数 [{}] 的值必须在 [{}] 中".format(field.name, field.enum_values)
                    )

        instance = cls(**parsed)
        return instance

    def process_args(self, **kwargs) -> Dict[Any, Any]:
        return self.as_dict()

    @classmethod
    def parse_and_process_args(cls, **kwargs) -> Dict[Any, Any]:
        return cls.parse_args().process_args(**kwargs)

    def as_dict(self) -> Dict[Any, Any]:
        return self.__storage__

    def get(self, item, default=None) -> Any:
        return self.__storage__.get(item, default)

    def __contains__(self, item):
        return item in self.__storage__

    def __str__(self):
        return "[<{}>: \n{}]".format(
            self.__class__.__name__, pprint.pformat(self.__storage__, indent=4)
        )


class NoArgs(BaseQueryModel):
    """this is usually used for get many"""

    pass
