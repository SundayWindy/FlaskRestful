from copy import copy
from uuid import uuid4

from tests import BaseTestCase


class TestComment(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestComment, cls).setUpClass()
        cls.url_prefix = "/api/topics/1/posts/1/comments"
        cls.root_topic = {"name": uuid4().hex}
        cls.client.post("/api/root_topics", json=cls.root_topic)
        cls.topic1 = {"name": uuid4().hex, "root_topic_id": 1}
        cls.posts1 = {"user_id": 1, "content": "this is post1"}
        cls.comment = {"user_id": 1, "content": "this is comment"}
        cls.client.post("/api/topics", json=cls.topic1)
        cls.client.post("/api/topics/1/posts", json=cls.posts1)

    def test_add_comment(self):
        self.client.post(self.url_prefix, json=self.comment)
        resp = self.client.get(self.url_prefix).json["data"]
        self.assertGreaterEqual(len(resp), 1)

    def test_add_comment_without_user(self):
        comment = copy(self.comment)
        comment.pop("user_id")
        resp = self.client.post(self.url_prefix, json=comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 400, "error_msg": "user_id 不能为 None"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_comment_with_invalid_content(self):
        comment = {"user_id": 1, "content": "     "}
        resp = self.client.post(self.url_prefix, json=comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 400, "error_msg": "不允许全部是空白字符，即至少有一个非空白字符"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_comment_with_post_or_topic_not_exist(self):
        resp = self.client.post("/api/topics/1000/posts/11/comments", json=self.comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 404, "error_msg": "Topic <1000> 不存在"}
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.post("/api/topics/1/posts/11/comments", json=self.comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 404, "error_msg": "Post <11> 不存在"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_comment(self):
        self.client.post(self.url_prefix, json=self.comment)
        resp = self.client.put(self.url_prefix + "/1", json=self.comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 403, "error_msg": "This operation is not allowed"}

        self.assertDictEqual(error_msg, expect_error_msg)

    def test_delete_comment(self):
        self.client.post(self.url_prefix, json=self.comment)
        resp = self.client.delete(self.url_prefix + "/1")

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 403, "error_msg": "This operation is not allowed"}

        self.assertDictEqual(error_msg, expect_error_msg)

    def test_get_comments(self):
        for i in range(1, 3):
            self.client.post("/api/topics/1/posts/1/comments", json=self.comment)

        post = self.client.get("/api/topics/1/posts/1").json["data"]
        self.assertGreaterEqual(post["comments_count"], 2)
        comments = self.client.get(self.url_prefix, json={"per_page": 1, "offset": 2}).json["data"]
        self.assertEqual(1, len(comments))
