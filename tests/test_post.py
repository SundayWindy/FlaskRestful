from tests import BaseTestCase


class TestPost(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url_prefix = '/api/topics/1/posts'

        self.root_topic = {'name': 'root_topic'}
        self.client.post('/api/root_topics', json=self.root_topic)
        self.topic1 = {'name': 'Topic1'}
        self.topic2 = {'name': 'Topic2'}
        self.user1 = {'email': 'hrui8005@gmail.com', 'password': '11Aa*%$#'}
        self.user2 = {'email': 'hrui8006@gmail.com', 'password': '11Aa*%$#'}
        self.posts1 = {'user_id': 1, 'content': 'this is post1'}
        self.posts2 = {'user_id': 1, 'content': 'this is post2'}

        self.client.post('/api/topics', json=self.topic1)
        self.client.post('/api/topics', json=self.topic2)
        self.client.post('/api/users', json=self.user1)
        self.client.post('/api/users', json=self.user2)

    def test_add_post(self):
        resp = self.client.get(self.url_prefix).json['data']
        self.assertEqual(0, len(resp))

        resp = self.client.post(self.url_prefix, json=self.posts1).json['data']
        data = {'user_id': resp['user_id'], 'content': resp['content']}
        self.assertEqual(self.posts1, data)

        posts = self.client.get(self.url_prefix).json['data']
        self.assertEqual(1, len(posts))

    def test_add_post_with_user_not_exist(self):
        self.posts1['user_id'] = 3
        resp = self.client.post(self.url_prefix, json=self.posts1)

        error_msg = resp.json
        error_msg.pop('traceback')
        expect_error_msg = {'error_code': 404, 'error_msg': 'User <3> 不存在'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_post_with_topic_not_exist(self):
        resp = self.client.post('/api/topics/3/posts', json=self.posts1)

        error_msg = resp.json
        error_msg.pop('traceback')
        expect_error_msg = {'error_code': 404, 'error_msg': 'Topic <3> 不存在'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_add_post_with_invalid_content(self):
        self.posts1['content'] = ''
        resp = self.client.post(self.url_prefix, json=self.posts1)

        error_msg = resp.json
        error_msg.pop('traceback')
        expect_error_msg = {'error_code': 400, 'error_msg': 'Post 文章字数不能少于 <5> 个'}
        self.assertDictEqual(error_msg, expect_error_msg)

    def test_update_post(self):
        self.client.post(self.url_prefix, json=self.posts1)

        new_post = {'user_id': 1, 'content': 'this is new post'}
        resp = self.client.put(self.url_prefix + '/1', json=new_post).json['data']

        data = {'user_id': resp['user_id'], 'content': resp['content']}
        self.assertEqual(new_post, data)

    def test_delete_post(self):
        self.client.post(self.url_prefix, json=self.posts1)
        self.client.post(self.url_prefix, json=self.posts2)

        resp = self.client.get(self.url_prefix).json['data']
        self.assertEqual(2, len(resp))

        self.client.delete(self.url_prefix + '/1')
        self.client.delete(self.url_prefix + '/2')

        resp = self.client.get(self.url_prefix).json['data']
        self.assertEqual(0, len(resp))

    def test_get_posts(self):
        posts = {'user_id': 1, 'content': ''}
        user = {'email': 'hrui8005@gmail.com', 'password': '11Aa*%$#'}
        self.client.post('/api/topics', json=self.topic1)
        self.client.post('/api/users', json=user)
        for i in range(1, 11):
            posts['content'] = 'this is post {}'.format(str(i))
            self.client.post('/api/topics/1/posts', json=posts)

        topics = self.client.get(self.url_prefix, json={'per_page': 2}).json['data']
        self.assertEqual(2, len(topics))

        topics = self.client.get(self.url_prefix, json={'per_page': 2, 'offset': 5}).json['data']
        self.assertEqual('this is post 6', topics[0]['content'])
