from exceptions import exceptions

from models.database_models.base_model import Base as Model


class BaseHandler:
    _model = None

    def __init__(self, id=None) -> None:
        self.id = id
        self.error_msg = f"{self._model.__name__} {self.id} 不存在"

    def assert_id_is_not_none(self) -> None:
        if self.id is None:
            raise exceptions.ServerException("id must not be None.")

    def _get_sqlalchemy_instance(self) -> Model:
        self.assert_id_is_not_none()
        instance = self._model.get_by_id(self.id)
        if not instance or getattr(instance, 'deleted', False):
            raise exceptions.ObjectsNotExist(self.error_msg)
        return instance
