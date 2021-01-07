from datetime import datetime
from uuid import uuid4

from tests import BaseTestCase


class TestUsers(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestUsers, cls).setUpClass()
        cls.url_prefix = "/api/users"

    def test_add_user(self):
        exist_user = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(exist_user), 1)

        new_user = {
            "email": "suepr76rui@icloud.com",
            "password": "b22sw1*#DJfyxoUaq",
            "create_time": datetime.now(),
        }
        self.client.post(self.url_prefix, json=new_user)
        users = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(users), 2)

    def test_add_user_with_wrong_password(self):
        new_user = {"email": uuid4().hex + "suepr76rui@icloud.com", "password": "111"}
        resp = self.client.post(self.url_prefix, json=new_user)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {
            "error_code": 400,
            "error_msg": "密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符,不能含有空格",
        }
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_with_wrong_email(self):
        new_user = {"email": uuid4().hex + "suepr76ruiicloud.com", "password": "111"}
        resp = self.client.post(self.url_prefix, json=new_user)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {"error_code": 400, "error_msg": "邮箱格式错误"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_without_email(self):
        new_user = {"password": "b22sw1*#DJfyxoUaq"}
        resp = self.client.post(self.url_prefix, json=new_user)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {"error_code": 400, "error_msg": "邮件地址不能为空"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_without_password(self):
        new_user = {"email": uuid4().hex + "suepr76rui@icloud.com"}
        resp = self.client.post(self.url_prefix, json=new_user)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {"error_code": 400, "error_msg": "密码不能为空"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_with_duplicate_email(self):
        email = uuid4().hex + "suepr76rui@icloud.com"
        new_user = {"email": email, "password": "b22sw1*#DJfyxoUaq"}
        self.client.post(self.url_prefix, json=new_user)
        users = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(users), 3)

        resp = self.client.post(self.url_prefix, json=new_user)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {"error_code": 403, "error_msg": f"邮件为 <{email}> 的用户已经注册"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_user_email(self):
        new_user = {"email": uuid4().hex + "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        res = self.client.post(self.url_prefix, json=new_user)

        kwargs = {"email": "hrui835@gmail.com"}
        user_id = res.json["data"]["id"]
        resp = self.client.put(self.url_prefix + f"/{user_id}", json=kwargs)

        expect_user = {
            "avatar": None,
            "company": None,
            "email": "hrui835@gmail.com",
            "id": user_id,
            "job": None,
            "name": None,
            "phone": None,
            "website": None,
        }

        update_user = resp.json["data"]
        self.assertEqual(200, resp.status_code)
        update_user.pop("update_time")
        update_user.pop("create_time")
        self.assertDictEqual(update_user, expect_user)

    def test_update_user_with_wrong_email(self):
        new_user = {"email": uuid4().hex + "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        res = self.client.post(self.url_prefix, json=new_user)

        user_id = res.json["data"]["id"]

        kwargs = {"email": "hrui835gmail.com"}
        resp = self.client.put(self.url_prefix + f"/{user_id}", json=kwargs)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {"error_code": 400, "error_msg": "邮箱格式错误"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_user_with_wrong_password(self):
        new_user = {"email": uuid4().hex + "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        res = self.client.post(self.url_prefix, json=new_user)
        user_id = res.json["data"]["id"]

        kwargs = {"password": "1111"}
        resp = self.client.put(self.url_prefix + f"/{user_id}", json=kwargs)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {
            "error_code": 400,
            "error_msg": "密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符,不能含有空格",
        }
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_delete(self):
        new_user = {"email": uuid4().hex + "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        self.client.post(self.url_prefix, json=new_user)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(4, len(resp))

        resp = self.client.delete(self.url_prefix + "/1")

        error_msg = resp.json
        expect_error_msg = {"data": {}, "error_code": 0, "error_msg": "success"}
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(3, len(resp))

    def test_get_user_not_existed(self):
        resp = self.client.get(self.url_prefix + "/100")

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {"error_code": 404, "error_msg": "用户 <100> 不存在"}
        self.assertDictEqual(error_msg, expect_error_msg)
