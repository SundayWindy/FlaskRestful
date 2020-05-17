from flask_restful import Resource

from handlers.user_handler import UserHandler
from models.query_models.user_model import UserQueryModel
from models.response_models.user_model import ResponseUserModel
from resources import ApiResponse, schema


class Users(Resource):
    @schema(query_model=UserQueryModel, response_model=ResponseUserModel)
    def get(self):
        # 获取所有的用户
        users = UserHandler.get_users()
        return ApiResponse().ok(users)

    @schema(query_model=UserQueryModel, response_model=ResponseUserModel)
    def post(self):
        # 新增一个用户
        kwargs = self.parsed_args
        user = UserHandler.create(**kwargs)
        return ApiResponse().ok(user)


class User(Resource):
    @schema(query_model=UserQueryModel, response_model=ResponseUserModel)
    def get(self, user_id):
        user = UserHandler(user_id).get_user()
        return ApiResponse().ok(user)

    @schema(query_model=UserQueryModel, response_model=ResponseUserModel)
    def put(self, user_id):
        kwargs = self.parsed_args
        user = UserHandler(user_id).update(**kwargs)
        return ApiResponse().ok(user)

    @schema(query_model=UserQueryModel, response_model=ResponseUserModel)
    def delete(self, user_id):
        UserHandler(user_id).delete()
        return ApiResponse().ok()
