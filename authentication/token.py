from flask import g
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource

from models.database_models.user_model import User

auth = HTTPBasicAuth()


# @auth.verify_password
# def verify_password(email, password):
#     user = User.query.filter_by(email=email).first()
#     if not user or not user.check_password(password):
#         return False
#     g.user = user
#     return True


class Token(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return {'token': token.decode('ascii')}


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    print('here', username_or_token)
    print(user)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(email=username_or_token).first()
        if not user or not user.check_password(password):
            return False
    g.user = user
    return True
