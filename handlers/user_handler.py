from typing import Generator, Optional
from werkzeug.security import generate_password_hash

from handlers.utils import EmailChecker, PassWordChecker
from handlers import BaseHandler
from models.database_models.user_model import User
from models.response_models.user_model import ResponseUserModel as ResponseUser

from exceptions.exceptions import ObjectsDuplicated, ArgumentInvalid, ArgumentRequired


class UserHandler(BaseHandler):
    _model = User

    def __init__(self, id: int = None) -> None:
        super().__init__(id)
        self.error_msg = f"用户 <{id}> 不存在"

    def get_user(self) -> ResponseUser:
        user = self._get_sqlalchemy_instance()
        return ResponseUser(**user.as_dict())

    @staticmethod
    def get_users() -> Generator[ResponseUser, None, None]:
        yield from (
            ResponseUser(**instance.as_dict()) for instance in User.query.filter_by(deleted=False)
        )

    @staticmethod
    def create(**kwargs) -> Optional[ResponseUser]:
        email = kwargs.get("email")
        password = kwargs.get("password")

        if not email:
            raise ArgumentRequired("邮件地址不能为空")
        user = User.query.filter_by(deleted=False).filter_by(email=email).first()
        if user:
            raise ObjectsDuplicated("邮件为 <%s> 的用户已经注册" % email)
        if password is None:
            raise ArgumentRequired("密码不能为空")
        password = password.strip()

        if not EmailChecker.is_allowed(email):
            raise ArgumentInvalid(EmailChecker.ERROR_MSG)

        if not PassWordChecker.is_allowed(password):
            raise ArgumentInvalid(PassWordChecker.ERROR_MSG)

        password_hash = generate_password_hash(password)

        kwargs.pop("password")
        kwargs.pop("email")

        ins = User.create(password_hash=password_hash, email=email, **kwargs)

        return ResponseUser(**ins.as_dict())

    def update(self, **kwargs) -> Optional[ResponseUser]:

        user = self._get_sqlalchemy_instance()
        email = kwargs.get("email")
        password = kwargs.get("password")

        if email and not EmailChecker.is_allowed(email):
            raise ArgumentInvalid(EmailChecker.ERROR_MSG)
            # 验证邮箱

        if password and not PassWordChecker.is_allowed(password):
            raise ArgumentInvalid(PassWordChecker.ERROR_MSG)
            # 验证密码，验证权限

        if password:
            password_hash = generate_password_hash(password)
            kwargs.pop("password")
            kwargs["password_hash"] = password_hash

        ins = user.update(**kwargs)

        return ResponseUser(**ins.as_dict())

    def delete(self) -> None:
        user = self._get_sqlalchemy_instance()
        user.update(deleted=True)

        return
