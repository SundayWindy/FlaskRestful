from tests import BaseTestCase


class TestComment(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url_prefix = "/api/topics/1/posts/1/comments"

        self.root_topic = {"name": "root_topic"}
        self.client.post("/api/root_topics", json=self.root_topic)
        self.topic1 = {"name": "Topic1", "root_topic_id": 1}
        self.posts1 = {"user_id": 1, "content": "this is post1"}
        self.user1 = {"email": "hrui8005@gmail.com", "password": "11Aa*%$#"}
        self.comment = {"user_id": 1, "content": "this is comment"}
        self.client.post("/api/topics", json=self.topic1)
        self.client.post("/api/users", json=self.user1)
        self.client.post("/api/topics/1/posts", json=self.posts1)

    def test_add_comment(self):
        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(0, len(resp))

        self.client.post(self.url_prefix, json=self.comment)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(1, len(resp))

    def test_add_comment_without_user(self):
        self.comment.pop("user_id")
        resp = self.client.post(self.url_prefix, json=self.comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {'error_code': 400, 'error_msg': 'user_id 不能为 None'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_comment_with_invalid_content(self):
        comment = {"user_id": 1, "content": "     "}
        resp = self.client.post(self.url_prefix, json=comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {'error_code': 400, 'error_msg': '不允许全部是空白字符，即至少有一个非空白字符'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_comment_with_post_or_topic_not_exist(self):
        resp = self.client.post("/api/topics/1000/posts/11/comments", json=self.comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {'error_code': 404, 'error_msg': 'Topic <1000> 不存在'}
        self.assertDictEqual(error_msg, expect_error_msg)

        resp = self.client.post("/api/topics/1/posts/11/comments", json=self.comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {'error_code': 404, 'error_msg': 'Post <11> 不存在'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_comment(self):
        self.client.post(self.url_prefix, json=self.comment)
        resp = self.client.put(self.url_prefix + "/1", json=self.comment)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {'error_code': 403, 'error_msg': "This operation is not allowed"}

        self.assertDictEqual(error_msg, expect_error_msg)

    def test_delete_comment(self):
        self.client.post(self.url_prefix, json=self.comment)
        resp = self.client.delete(self.url_prefix + "/1")

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {'error_code': 403, 'error_msg': "This operation is not allowed"}

        self.assertDictEqual(error_msg, expect_error_msg)

    def test_get_comments(self):
        for i in range(1, 11):
            self.comment["content"] = str(i)
            self.client.post("/api/topics/1/posts/1/comments", json=self.comment)

        post = self.client.get("/api/topics/1/posts/1").json["data"]
        self.assertEqual(10, post["comments_count"])

        comments = self.client.get(self.url_prefix, json={"per_page": 2}).json["data"]
        self.assertEqual(2, len(comments))

        comments = self.client.get(self.url_prefix, json={"per_page": 3, "offset": 5}).json["data"]
        self.assertEqual("6", comments[0]["content"])
