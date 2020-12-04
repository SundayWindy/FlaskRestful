from models.database import RootTopic
from tests import BaseTestCase


class TestRootTopic(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url_prefix = "/api/root_topics"
        self.root_topic1 = {"name": "root_topic1"}
        self.root_topic2 = {"name": "root_topic2"}
        self.topic1 = {"name": "Topic1"}
        self.topic2 = {"name": "Topic2"}
        self.topic3 = {"name": "Topic3"}

    def tearDown(self) -> None:
        with self.app.app_context():
            RootTopic.query.delete()

    def test_add_root_topic(self):
        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(1, len(resp))

        self.client.post(self.url_prefix, json=self.root_topic1)
        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(1, len(resp))
        self.assertEqual(self.root_topic1["name"], resp[0]["name"])

    def test_put_root_topic(self):
        self.client.post(self.url_prefix, json=self.root_topic1)
        new_root_topic = {"name": "new_root_topic1"}
        self.client.put(self.url_prefix + "/1", json=new_root_topic)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(1, len(resp))
        self.assertEqual(new_root_topic["name"], resp[0]["name"])

    def test_delete_root_topic(self):
        self.client.post(self.url_prefix, json=self.root_topic1)

        resp = self.client.delete(self.url_prefix + "/1")
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 403, 'error_msg': '根主题不允许被删除'}
        self.assertDictEqual(expect_error_msg, error_msg)

    def test_add_invalid_root_topic(self):
        self.client.post(self.url_prefix, json=self.root_topic1)

        new_root_topic = {"name": "root_topic1"}
        resp = self.client.post(self.url_prefix, json=new_root_topic)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 403, 'error_msg': '名称为 <root_topic1> 的根 Topic 已经创建'}
        self.assertDictEqual(expect_error_msg, error_msg)

        new_root_topic = {"name": ""}
        resp = self.client.post(self.url_prefix, json=new_root_topic)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {
            'error_code': 400,
            'error_msg': '名称中只允许出现【中文，英文，数字，下划线，连接符】,并且不允许全部是空白字符',
        }
        self.assertDictEqual(expect_error_msg, error_msg)

        new_root_topic = {}
        resp = self.client.post(self.url_prefix, json=new_root_topic)
        error_msg = resp.json
        error_msg.pop("traceback")

        expect_error_msg = {'error_code': 400, 'error_msg': '根主题名不能为空'}
        self.assertDictEqual(expect_error_msg, error_msg)
