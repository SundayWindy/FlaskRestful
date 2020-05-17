from models.base_model import BaseModel


class BaseResponseModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class NoValue(BaseResponseModel):
    pass
