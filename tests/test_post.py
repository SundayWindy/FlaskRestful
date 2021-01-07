from uuid import uuid4

from tests import BaseTestCase


class TestPost(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestPost, cls).setUpClass()
        cls.url_prefix = "/api/topics/1/posts"
        cls.root_topic = {"name": uuid4().hex}
        cls.client.post("/api/root_topics", json=cls.root_topic)
        cls.topic1 = {"name": uuid4().hex}
        cls.topic2 = {"name": uuid4().hex}
        cls.user1 = {"email": uuid4().hex + "hrui8005@gmail.com", "password": "11Aa*%$#"}
        cls.user2 = {"email": uuid4().hex + "hrui8006@gmail.com", "password": "11Aa*%$#"}
        cls.posts1 = {"user_id": 1, "content": "this is post1"}
        cls.posts2 = {"user_id": 1, "content": "this is post2"}
        cls.client.post("/api/topics", json=cls.topic1)
        cls.client.post("/api/topics", json=cls.topic2)
        cls.client.post("/api/users", json=cls.user1)
        cls.client.post("/api/users", json=cls.user2)

    def test_add_post(self):
        resp = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(0, len(resp))

        resp = self.client.post(self.url_prefix, json=self.posts1).json["data"]
        data = {"user_id": resp["user_id"], "content": resp["content"]}
        self.assertEqual(self.posts1, data)

        posts = self.client.get(self.url_prefix).json["data"]
        self.assertEqual(1, len(posts))

    def test_add_post_with_user_not_exist(self):
        self.posts1["user_id"] = 300
        resp = self.client.post(self.url_prefix, json=self.posts1)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 404, "error_msg": "User <300> 不存在"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_post_with_topic_not_exist(self):
        resp = self.client.post("/api/topics/300/posts", json=self.posts1)

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 404, "error_msg": "Topic <300> 不存在"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_post_with_invalid_content(self):
        resp = self.client.post(self.url_prefix, json={"user_id": 1, "content": ""})

        error_msg = resp.json
        error_msg.pop("traceback")
        expect_error_msg = {"error_code": 400, "error_msg": "Post 文章字数不能少于 <5> 个"}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_post(self):
        res = self.client.post(self.url_prefix, json={"user_id": 1, "content": "this is post1"})

        new_post = {"user_id": 1, "content": "this is new post"}
        resp = self.client.put(self.url_prefix + f"/{res.json['data']['id']}", json=new_post).json[
            "data"
        ]

        data = {"user_id": resp["user_id"], "content": resp["content"]}
        self.assertEqual(new_post, data)

    def test_delete_post(self):
        self.client.post(self.url_prefix, json=self.posts1)
        self.client.post(self.url_prefix, json=self.posts2)

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertGreaterEqual(len(resp), 2)

        self.client.delete(self.url_prefix + "/1")
        self.client.delete(self.url_prefix + "/2")

        resp = self.client.get(self.url_prefix).json["data"]
        self.assertLessEqual(0, len(resp))

    def test_get_posts(self):
        posts = {"user_id": 1, "content": ""}
        user = {"email": uuid4().hex + "hrui8005@gmail.com", "password": "11Aa*%$#"}
        self.client.post("/api/topics", json={"name": uuid4().hex})
        self.client.post("/api/users", json=user)
        for i in range(1, 3):
            posts["content"] = "this is post {}".format(str(i))
            self.client.post("/api/topics/1/posts", json=posts)

        topics = self.client.get(self.url_prefix, json={"per_page": 2}).json["data"]
        self.assertEqual(2, len(topics))
