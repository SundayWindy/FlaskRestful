import pprint

from flask_restful import reqparse
from typing import Callable, TypeVar, Dict, Any

from exceptions.exceptions import ArgumentInvalid
from models.base_model import ApiDataType, BaseModel, Field

T = TypeVar("T", bound=BaseModel)


class QueryField(Field):
    __slots__ = (
        'name',
        'field_type',
        'mock_func',
        'enum_values',
        'description',
        'nullable',
        'required',
        'location',
        'default',
        'parser_kwargs',
        'parse_func',
    )

    def __init__(
            self,
            field_type: ApiDataType,
            location: str,
            parser_func: Callable = None,
            required: bool = False,
            mock_func: bool = False,
            enum_values: tuple = (),
            comment: str = "",
            nullable: bool = True,
            **kwargs
    ) -> None:
        super().__init__(field_type, mock_func, enum_values, comment, nullable)
        self.location = location
        self.parser_kwargs = kwargs
        self.required = required
        self.parse_func = parser_func or self.field_type.marshal
        if 'default' in kwargs:
            self.default = kwargs['default']


class BaseQueryModel(BaseModel):
    def __init__(self, **kwargs: dict):
        super().__init__(drop_missing=False, **kwargs)
        self.__storage__ = kwargs
        for field_name in self.__fields_map__.keys():
            if field_name not in self.__storage__:
                delattr(self, field_name)

    @classmethod
    def parse_args(cls) -> T:
        parser = reqparse.RequestParser()

        for field in cls.__fields__:
            name = field.name
            location = field.location
            required = field.required
            nullable = field.nullable
            parser.add_argument(
                name, location=location, required=required, nullable=nullable, **field.parser_kwargs
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
        return '[<{}>: \n{}]'.format(
            self.__class__.__name__, pprint.pformat(self.__storage__, indent=4)
        )


class NoArgs(BaseQueryModel):
    pass
