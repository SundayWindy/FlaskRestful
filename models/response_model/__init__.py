from models import BaseModel


class BaseResponseModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
