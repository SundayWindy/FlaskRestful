from datetime import datetime
from tests import BaseTestCase


class TestUsers(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url_prefix = "/api/users"

    def test_add_user(self):
        exist_user = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(exist_user), 0)

        new_user = {"email": "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq", "create_time": datetime.now()}
        self.client.post(self.url_prefix, json=new_user)
        users = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(users), 1)

    def test_add_user_with_wrong_password(self):
        new_user = {"email": "suepr76rui@icloud.com", "password": "111"}
        resp = self.client.post(self.url_prefix, json=new_user)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {
            'error_code': 400,
            'error_msg': '密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符,不能含有空格',
        }
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_with_wrong_email(self):
        new_user = {"email": "suepr76ruiicloud.com", "password": "111"}
        resp = self.client.post(self.url_prefix, json=new_user)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 400, 'error_msg': '邮箱格式错误'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_without_email(self):
        new_user = {"password": "b22sw1*#DJfyxoUaq"}
        resp = self.client.post(self.url_prefix, json=new_user)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 403, 'error_msg': '邮件地址不能为空'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_without_password(self):
        new_user = {"email": "suepr76rui@icloud.com"}
        resp = self.client.post(self.url_prefix, json=new_user)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 403, 'error_msg': '密码不能为空'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_user_with_duplicate_email(self):
        new_user = {"email": "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        self.client.post(self.url_prefix, json=new_user)
        users = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(len(users), 1)

        resp = self.client.post(self.url_prefix, json=new_user)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 403, 'error_msg': '邮件为 <suepr76rui@icloud.com> 的用户已经注册'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_user_email(self):
        new_user = {"email": "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        self.client.post(self.url_prefix, json=new_user)

        kwargs = {"email": "hrui835@gmail.com"}
        resp = self.client.put(self.url_prefix + "/1", json=kwargs)

        expect_user = {
            'About_me': None,
            'BTC_Address': None,
            'BattleTag': None,
            'Coding_net': None,
            'Dribbble': None,
            'Duolingo': None,
            'GitHub': None,
            'Goodreads': None,
            'Instagram': None,
            'Last_me': None,
            'PSN_ID': None,
            'Personal_Introduction': None,
            'Steam_ID': None,
            'Telegram': None,
            'Twitch': None,
            'Twitter': None,
            'avatar': None,
            'community_rich_rank': None,
            'company': None,
            'email': 'hrui835@gmail.com',
            'id': 1,
            'job': None,
            'location': None,
            'money': None,
            'name': None,
            'phone': None,
            'show_remain_money': None,
            'signature': None,
            'state_update_view_permission': None,
            'time_zone': None,
            'use_avatar_for_favicon': None,
            'use_high_resolution_avatar': None,
            'website': None,
        }

        update_user = resp.json["data"]
        self.assertEqual(200, resp.status_code)
        self.assertDictEqual(update_user, expect_user)

    def test_update_user_with_wrong_email(self):
        new_user = {"email": "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        self.client.post(self.url_prefix, json=new_user)

        kwargs = {"email": "hrui835gmail.com"}
        resp = self.client.put(self.url_prefix + "/1", json=kwargs)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 400, 'error_msg': '邮箱格式错误'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_user_with_wrong_password(self):
        new_user = {"email": "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        self.client.post(self.url_prefix, json=new_user)

        kwargs = {"password": "1111"}
        resp = self.client.put(self.url_prefix + "/1", json=kwargs)

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {
            'error_code': 400,
            'error_msg': '密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符,不能含有空格',
        }
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_delete(self):
        new_user = {"email": "suepr76rui@icloud.com", "password": "b22sw1*#DJfyxoUaq"}
        self.client.post(self.url_prefix, json=new_user)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(1, len(resp))

        resp = self.client.delete(self.url_prefix + "/1")

        error_msg = resp.json
        expect_error_msg = {'data': {}, 'error_code': 0, 'error_msg': 'success'}
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(0, len(resp))

    def test_get_user_not_existed(self):
        resp = self.client.get(self.url_prefix + "/1")

        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 404, 'error_msg': '用户 <1> 不存在'}
        self.assertDictEqual(error_msg, expect_error_msg)
