from exceptions import exceptions
from models.database_model import Base as Model


class BaseHandler:
    _model = None

    def __init__(self, id=None):
        self.id = id

    def get_sqlalchemy_instance(self, error_msg=None) -> Model:
        if self.id is None:
            raise exceptions.ServerException("id must not be None.")
        instance = self._model.get_by_id(self.id)
        if not instance or getattr(instance, 'deleted', False):
            if not error_msg:
                error_msg = "{model} {id} 不存在".format(model=self._model.__name__, id=self.id)
            raise exceptions.ObjectsNotExisted(error_msg)
        return instance
