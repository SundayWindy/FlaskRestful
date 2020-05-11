from flask_restful import Resource

from handlers.user_handler import UserHandler


class Users(Resource):
    def get(self):
        # 获取所有的用户
        return [user.marshal() for user in UserHandler.get_users()]

    def post(self):
        pass


class User(Resource):
    def get(self, user_id):
        pass

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass
