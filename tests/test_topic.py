from tests import BaseTestCase


class TestTopics(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url_prefix = "/api/topics"
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
        self.assertDictEqual(self.topic1, resp)

    def test_add_topic_with_invalid_name(self):
        resp = self.client.post(self.url_prefix, json=self.topic4)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 400, 'error_msg': '名称中只允许出现【中文，英文，数字，下换线，连接符'}
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

        expect_error_msg = {'error_code': 400, 'error_msg': '名称中只允许出现【中文，英文，数字，下换线，连接符'}
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.put(self.url_prefix + "/2", json=self.topic5)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 400, 'error_msg': '名称中只允许出现【中文，英文，数字，下换线，连接符'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_delete_topic(self):
        self.client.post(self.url_prefix, json=self.topic1)
        self.client.post(self.url_prefix, json=self.topic2)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(2, len(resp))

        self.client.delete(self.url_prefix + "/1")

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(1, len(resp))
