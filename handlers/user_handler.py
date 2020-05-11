from werkzeug.security import generate_password_hash, check_password_hash

from exceptions import exceptions
from models.database_model.user_model import User
from models.response_model.user_model import UserModel as ResponseUser
from configures.help_funcs import EmailChecker


class UserHandler:
    model = User

    @staticmethod
    def get_user(user_id):
        user = User.query.filter_by(deleted=False).filter_by(id=user_id).first()
        return [] if not user else ResponseUser(**user.as_dict())

    @staticmethod
    def get_users():
        return [ResponseUser(**instance.as_dict()) for instance in User.query]

    @staticmethod
    def create_user(**kwargs):
        email = kwargs.get("email")
        password = kwargs.get("password")

        if not email:
            raise exceptions.ArgumentRequiredException("邮件地址不能为空")
        if not password:
            raise exceptions.ArgumentRequiredException("密码不能为空")

        password = password.strip()
        if len(password) <= 6:
            raise exceptions.InvalidArgumentException("密码不能少于 8 位")

        if not EmailChecker.is_allowed(email):
            raise exceptions.InvalidArgumentException(EmailChecker.ERROR_MSG)
        password_hash = generate_password_hash(password)

        kwargs.pop(password)
        kwargs.pop(email)

        ins = User.create(password_hash=password_hash, email=email, **kwargs)

        return ResponseUser(**ins.as_dict())
