from werkzeug.security import generate_password_hash, check_password_hash

from exceptions import exceptions
from models.database_model.user_model import User
from models.response_model.user_model import UserModel as ResponseUser
from configures.help_funcs import EmailChecker, PassWordChecker

from handlers import BaseHandler


class UserHandler(BaseHandler):
    _model = User

    def __init__(self, id=None):
        super().__init__(id)
        self.error_msg = "用户 <%s> 不存在" % id

    def get_user(self):
        user = self.get_sqlalchemy_instance(self.error_msg)
        return ResponseUser(**user.as_dict())

    @staticmethod
    def get_users():
        yield from (ResponseUser(**instance.as_dict()) for instance in User.query.filter_by(deleted=False))

    @staticmethod
    def create(**kwargs):
        email = kwargs.get("email")
        password = kwargs.get("password")

        if not email:
            raise exceptions.ArgumentRequired("邮件地址不能为空")
        user = User.query.filter_by(deleted=False).filter_by(email=email).first()
        if user:
            raise exceptions.ObjectsDuplicated("邮件为 <%s> 的用户已经注册" % email)

        password = password.strip()

        if not EmailChecker.is_allowed(email):
            raise exceptions.InvalidArgument(EmailChecker.ERROR_MSG)

        if not PassWordChecker.is_allowed(password):
            raise exceptions.InvalidArgument(PassWordChecker.ERROR_MSG)

        password_hash = generate_password_hash(password)

        kwargs.pop("password")
        kwargs.pop("email")

        ins = User.create(password_hash=password_hash, email=email, **kwargs)

        return ResponseUser(**ins.as_dict())

    def update(self, **kwargs):

        user = self.get_sqlalchemy_instance(self.error_msg)
        email = kwargs.get("email")
        password = kwargs.get("password")

        if email and not EmailChecker.is_allowed(email):
            raise exceptions.InvalidArgument(EmailChecker.ERROR_MSG)
            # 验证邮箱

        if password and not PassWordChecker.is_allowed(password):
            raise exceptions.InvalidArgument(PassWordChecker.ERROR_MSG)
            # 验证密码，验证权限

        password_hash = generate_password_hash(password)

        kwargs.pop("password")
        kwargs.pop("email")

        ins = user.update(password_hash=password_hash, email=email, **kwargs)

        return ResponseUser(**ins.as_dict())

    def delete(self):
        user = self.get_sqlalchemy_instance(self.error_msg)
        user.update(deleted=True)

        return
