from exceptions import exceptions
from typing import Type, TypeVar

from models.database import Base as Model

U = TypeVar('U', bound=Model)


class BaseHandler:
    _model = None

    def __init__(self, id=None) -> None:
        self.id = id
        self.error_msg = f"{self._model.__name__} {self.id} 不存在"

    def assert_id_is_not_none(self) -> None:
        if self.id is None:
            raise exceptions.ServerException("id must not be None.")

    def _get_sqlalchemy_instance(self) -> Type[U]:
        self.assert_id_is_not_none()
        instance = self._model.get_by_id(self.id)
        if not instance or getattr(instance, 'deleted', False):
            raise exceptions.ObjectsNotExist(self.error_msg)
        return instance
