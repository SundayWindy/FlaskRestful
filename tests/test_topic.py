from tests import BaseTestCase


class TestTopics(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url_prefix = "/api/topics"
        self.root_topic = {"name": "root_topic"}
        self.client.post("/api/root_topics", json=self.root_topic)
        self.topic1 = {"name": "Topic1"}
        self.topic2 = {"name": "Topic2"}
        self.topic3 = {"name": "Topic3"}
        self.topic4 = {"name": ""}
        self.topic5 = {"name": "abc&^%3"}
        self.topic6 = {"name": "update"}

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

        expect_error_msg = {'error_code': 400, 'error_msg': '名称中只允许出现【中文，英文，数字，下划线，连接符】,并且不允许全部是空白字符'}
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

        expect_error_msg = {'error_code': 403, 'error_msg': '名称为 <Topic1> 的 Topic 已经创建'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_topic(self):
        self.client.post(self.url_prefix, json=self.topic1)

        resp = self.client.put(self.url_prefix + "/1", json=self.topic6).json["data"]
        resp.pop("id")
        self.topic6["posts_count"] = 0
        self.assertDictEqual(self.topic6, resp)

    def test_update_topic_with_invalid_name(self):
        self.client.post(self.url_prefix, json=self.topic1)
        self.client.post(self.url_prefix, json=self.topic2)

        resp = self.client.put(self.url_prefix + "/2", json=self.topic1)  # topic1 已经被创建
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 403, 'error_msg': '名称为 <Topic1> 的 Topic 已经创建'}
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.put(self.url_prefix + "/2", json=self.topic4)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 400, 'error_msg': '名称中只允许出现【中文，英文，数字，下划线，连接符】,并且不允许全部是空白字符'}
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.put(self.url_prefix + "/2", json=self.topic5)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 400, 'error_msg': '名称中只允许出现【中文，英文，数字，下划线，连接符】,并且不允许全部是空白字符'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_delete_topic(self):
        self.client.post(self.url_prefix, json=self.topic1)
        self.client.post(self.url_prefix, json=self.topic2)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(2, len(resp))

        self.client.delete(self.url_prefix + "/1")

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(1, len(resp))

    def test_get_topic_with_some_posts(self):
        self.client.post("/api/topics", json={"name": "Topic1"})  # create topic
        self.client.post("/api/users", json={"email": "hrui8005@gmail.com", "password": "11Aa*%$#"})  # create user

        posts = {"user_id": 1, "content": "this is post1"}
        for _ in range(10):
            self.client.post("/api/topics/1/posts", json=posts)

        resp = self.client.get(self.url_prefix).json["data"]

        expect = [{'id': 1, 'name': 'Topic1', 'posts_count': 10}]
        self.assertListEqual(expect, resp)
