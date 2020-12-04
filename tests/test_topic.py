from uuid import uuid4

from models.database import Topic
from tests import BaseTestCase


class TestTopics(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url_prefix = "/api/topics"
        self.root_topic = {"name": uuid4().hex}
        self.client.post("/api/root_topics", json=self.root_topic)
        self.topic1 = {"name": uuid4().hex}
        self.topic2 = {"name": uuid4().hex}
        self.topic3 = {"name": uuid4().hex}
        self.topic4 = {"name": ""}
        self.topic5 = {"name": "abc&^%3"}
        self.topic6 = {"name": "update"}

    def tearDown(self) -> None:
        with self.app.app_context():
            Topic.query.delete()

    def test_add_topic(self):
        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(0, len(resp))

        resp = self.client.post(self.url_prefix, json=self.topic1).json["data"]
        resp.pop("id")
        self.topic1["posts_count"] = 0
        self.assertDictEqual(self.topic1, resp)

    def test_add_topic_with_invalid_name(self):
        resp = self.client.post(self.url_prefix, json=self.topic4)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {
            'error_code': 400,
            'error_msg': '名称中只允许出现【中文，英文，数字，下划线，连接符】,并且不允许全部是空白字符',
        }
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.post(self.url_prefix, json=self.topic5)
        error_msg = resp.json
        error_msg.pop("traceback")
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_topic_with_exist_name(self):
        self.client.post(self.url_prefix, json=self.topic1)
        resp = self.client.post(self.url_prefix, json=self.topic1)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 403, 'error_msg': f'名称为 <{self.topic1["name"]}> 的 Topic 已经创建'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_topic(self):
        self.client.post(self.url_prefix, json=self.topic1)

        resp = self.client.put(self.url_prefix + "/1", json=self.topic6).json["data"]
        resp.pop("id")
        self.topic6["posts_count"] = 10
        self.assertDictEqual(self.topic6, resp)

    def test_update_topic_with_invalid_name(self):
        self.client.post(self.url_prefix, json=self.topic1)
        self.client.post(self.url_prefix, json=self.topic2)

        resp = self.client.put(self.url_prefix + "/2", json=self.topic1)  # topic1 已经被创建
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 403, 'error_msg': f'名称为 <{self.topic1["name"]}> 的 Topic 已经创建'}
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.put(self.url_prefix + "/2", json=self.topic4)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {
            'error_code': 400,
            'error_msg': '名称中只允许出现【中文，英文，数字，下划线，连接符】,并且不允许全部是空白字符',
        }
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.put(self.url_prefix + "/2", json=self.topic5)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {
            'error_code': 400,
            'error_msg': '名称中只允许出现【中文，英文，数字，下划线，连接符】,并且不允许全部是空白字符',
        }
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_delete_topic(self):
        res = self.client.post(self.url_prefix, json=self.topic1)
        self.client.post(self.url_prefix, json=self.topic2)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(4, len(resp))

        self.client.delete(self.url_prefix + f"/{res.json['data']['id']}")

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertLessEqual(1, len(resp))

    def test_get_topic_with_some_posts(self):
        self.client.post("/api/topics", json={"name": "Topic1"})  # create topic
        self.client.post(
            "/api/users", json={"email": uuid4().hex + "hrui8005@gmail.com", "password": "11Aa*%$#"}
        )  # create user

        posts = {"user_id": 1, "content": "this is post1"}
        for _ in range(10):
            self.client.post("/api/topics/1/posts", json=posts)

        resp = self.client.get(self.url_prefix).json["data"]

        self.assertEqual(10, resp[0]["posts_count"])
