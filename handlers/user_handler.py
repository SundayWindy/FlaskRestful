from exceptions import exceptions

from werkzeug.security import check_password_hash, generate_password_hash

from configures.help_funcs import EmailChecker, PassWordChecker
from handlers import BaseHandler
from models.database_models.user_model import User
from models.response_models.user_model import ResponseUserModel as ResponseUser


class UserHandler(BaseHandler):
    _model = User

    def __init__(self, id=None):
        super().__init__(id)
        self.error_msg = f"用户 <{id}> 不存在"

    def get_user(self):
        user = self.get_sqlalchemy_instance()
        return ResponseUser(**user.as_dict())

    @staticmethod
    def get_users():
        yield from (
            ResponseUser(**instance.as_dict()) for instance in User.query.filter_by(deleted=False)
        )

    @staticmethod
    def create(**kwargs):
        email = kwargs.get("email")
        password = kwargs.get("password")

        if not email:
            raise exceptions.ArgumentRequired("邮件地址不能为空")
        user = User.query.filter_by(deleted=False).filter_by(email=email).first()
        if user:
            raise exceptions.ObjectsDuplicated("邮件为 <%s> 的用户已经注册" % email)

        if password is None:
            raise exceptions.ArgumentRequired("密码不能为空")
        password = password.strip()

        if not EmailChecker.is_allowed(email):
            raise exceptions.ArgumentInvalid(EmailChecker.ERROR_MSG)

        if not PassWordChecker.is_allowed(password):
            raise exceptions.ArgumentInvalid(PassWordChecker.ERROR_MSG)

        password_hash = generate_password_hash(password)

        kwargs.pop("password")
        kwargs.pop("email")

        ins = User.create(password_hash=password_hash, email=email, **kwargs)

        return ResponseUser(**ins.as_dict())

    def update(self, **kwargs):

        user = self.get_sqlalchemy_instance()
        email = kwargs.get("email")
        password = kwargs.get("password")

        if email and not EmailChecker.is_allowed(email):
            raise exceptions.ArgumentInvalid(EmailChecker.ERROR_MSG)
            # 验证邮箱

        if password and not PassWordChecker.is_allowed(password):
            raise exceptions.ArgumentInvalid(PassWordChecker.ERROR_MSG)
            # 验证密码，验证权限

        if password:
            password_hash = generate_password_hash(password)
            kwargs.pop("password")
            kwargs["password_hash"] = password_hash

        ins = user.update(**kwargs)

        return ResponseUser(**ins.as_dict())

    def delete(self):
        user = self.get_sqlalchemy_instance()
        user.update(deleted=True)

        return
