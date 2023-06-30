import inspect
from functools import wraps
from typing import Any, Callable, Dict, TypeVar

from flask import jsonify

from models.query_models.base_model import BaseQueryModel
from models.response_models.base_model import NoValue, BaseResponseModel

schema_mapping = {}
Api = TypeVar('Api')


class ResourceSchema:
    def __init__(self, query_model: type[BaseQueryModel], response_model: type[BaseResponseModel],
                 path_parameters) -> None:
        self.query_model = query_model
        self.response_model = response_model
        self.path_parameters = path_parameters


def schema(query_model: type[BaseQueryModel], response_model: type[BaseResponseModel]):
    def decorator(func):
        params = list(inspect.signature(func).parameters)
        params.remove('self')
        schema_mapping[func.__qualname__] = ResourceSchema(query_model, response_model, params)

        @wraps(func)
        def wrapper(self, **kwargs) -> Callable:
            """args in path occurs in kwargs"""
            self.query_model = query_model
            self.response_model = response_model
            self.parsed_args = self.query_model.parse_and_process_args(**kwargs)
            return jsonify(func(self, **kwargs))

        return wrapper

    return decorator


class ApiResponse:
    def __init__(self) -> None:
        self.data = {}
        self.error_code = None
        self.error_msg = None

    def ok(self, data: Any = None) -> Api:
        self.set_data(data)
        self.error_code = 0
        self.error_msg = 'success'
        return self

    def error(self, error_code, error_msg) -> Api:
        self.error_code = error_code
        self.error_msg = error_msg
        return self

    def set_data(self, data) -> Api:
        if data is None or data == {}:
            data = NoValue()
        self.data = data
        return self

    def get(self) -> Dict[str, Any]:
        if self.error_code is None or self.error_msg is None:
            raise Exception('ApiResponse not ready.')
        return {
            'data': self.data,
            'error_code': self.error_code,
            'error_msg': self.error_msg,
        }
