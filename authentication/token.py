import logging

from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from flask_restful import Resource

from models.orm import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()
auth = MultiAuth(basic_auth, token_auth)


class Token(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return {"token": token.decode("ascii")}


@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(email=username).first()
    if not user or not user.check_password(password):
        return False
    logging.info(f"用户 <{user}> 登陆>")
    g.user = user
    return True


@token_auth.verify_token
def verify_token(token):
    try:
        user = User.verify_auth_token(token)
    except:  # noqa
        return False
    else:
        g.user = user
        return user
