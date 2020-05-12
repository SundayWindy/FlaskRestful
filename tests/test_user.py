from exceptions import exceptions
from tests import BaseTestCase


class TestUsers(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.url_prefix = "/api/users"

    def test_add_user(self):
        exist_user = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(exist_user), 0)

        new_user = {"email": "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        self.client.post(self.url_prefix, json=new_user)
        users = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(users), 1)

    def test_add_user_with_wrong_password(self):
        exist_user = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(exist_user), 0)

        new_user = {"email": "suepr76rui@icloud.com", "password": "111"}
        resp = self.client.post(self.url_prefix, json=new_user)
        self.assertEqual(400, resp.status_code)
        expect_error_msg = {'error_code': 400, 'error_msg': '至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符,不能含有空格'}
        error_msg = resp.json
        error_msg.pop("traceback")

        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_with_wrong_email(self):
        exist_user = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(exist_user), 0)

        new_user = {"email": "suepr76ruiicloud.com", "password": "111"}
        resp = self.client.post(self.url_prefix, json=new_user)
        self.assertEqual(400, resp.status_code)

        expect_error_msg = {'error_code': 400, 'error_msg': '邮箱格式错误'}
        error_msg = resp.json
        error_msg.pop("traceback")

        self.assertDictEqual(error_msg, expect_error_msg)
