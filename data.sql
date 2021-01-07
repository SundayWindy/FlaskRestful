create database IF NOT EXISTS flask_restful;

use flask_restful;


create table comment
(
    id          int auto_increment
        primary key,
    user_id     int                                  not null comment '评论用户的 ID',
    post_id     int                                  not null comment 'Post 文章的 ID',
    content     text                                 not null comment '用户的评论',
    create_time datetime   default CURRENT_TIMESTAMP null comment '创建时间',
    update_time datetime   default CURRENT_TIMESTAMP null comment '更新时间',
    deleted     tinyint(1) default 0                 not null comment '该项目是否被删除'
);

INSERT INTO flask_restful.comment (id, user_id, post_id, content, create_time, update_time, deleted) VALUES (1, 1, 1, 'this comment is for testing', '2020-05-23 03:55:28', '2020-05-23 03:55:28', 0);
INSERT INTO flask_restful.comment (id, user_id, post_id, content, create_time, update_time, deleted) VALUES (2, 1, 1, 'this comment is for testing', '1970-01-01 00:00:00', null, 0);
INSERT INTO flask_restful.comment (id, user_id, post_id, content, create_time, update_time, deleted) VALUES (3, 1, 1, 'this comment is for testing', '2020-05-23 15:32:49', '2020-05-23 15:32:49', 0);
INSERT INTO flask_restful.comment (id, user_id, post_id, content, create_time, update_time, deleted) VALUES (4, 1, 1, 'this comment is for testing', '2020-05-23 15:32:49', '2020-05-23 15:32:49', 0);
INSERT INTO flask_restful.comment (id, user_id, post_id, content, create_time, update_time, deleted) VALUES (5, 1, 1, 'this comment is for testing', '2020-05-23 15:32:49', '2020-05-23 15:32:49', 0);
INSERT INTO flask_restful.comment (id, user_id, post_id, content, create_time, update_time, deleted) VALUES (6, 1, 1, 'this comment is for testing', '2020-05-23 15:32:49', '2020-05-23 15:32:49', 0);
INSERT INTO flask_restful.comment (id, user_id, post_id, content, create_time, update_time, deleted) VALUES (7, 1, 1, 'this comment is for testing', '2020-05-23 15:32:49', '2020-05-23 15:32:49', 0);
create table post
(
    id          int auto_increment
        primary key,
    topic_id    int                                  not null comment '文章所在的主题 ID',
    user_id     int                                  not null comment '发布文章用户的 ID',
    content     text                                 not null,
    click_times int                                  null comment '文章的点击数',
    tags        json                                 null comment '文章的 tag',
    create_time datetime   default CURRENT_TIMESTAMP null comment '创建时间',
    update_time datetime   default CURRENT_TIMESTAMP null comment '更新时间',
    deleted     tinyint(1) default 0                 not null comment '该项目是否被删除'
);

INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (1, 1, 1, '"this post is for testing1"', null, null, '2020-05-23 03:55:10', '2020-05-23 03:55:10', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (2, 1, 1, '"this post is for testing2"', null, null, '2020-05-23 03:55:10', '2020-05-23 03:55:10', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (3, 1, 1, '"this post is for testing3"', null, null, '2020-05-23 03:55:10', '2020-05-23 03:55:10', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (4, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (5, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (6, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (7, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (8, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (9, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (10, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (11, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
INSERT INTO flask_restful.post (id, topic_id, user_id, content, click_times, tags, create_time, update_time, deleted) VALUES (12, 1, 1, '"this post is for testing"', null, null, '2020-05-23 15:32:18', '2020-05-23 15:32:18', 0);
create table root_topic
(
    id          int auto_increment
        primary key,
    name        varchar(256)                         not null,
    create_time datetime   default CURRENT_TIMESTAMP null comment '创建时间',
    update_time datetime   default CURRENT_TIMESTAMP null comment '更新时间',
    deleted     tinyint(1) default 0                 not null comment '该项目是否被删除'
);

INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (1, '分享与探索', '2020-05-22 13:47:10', '2020-05-22 13:47:10', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (2, '机器学习', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (3, '前端开发', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (4, '编程语言', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (5, '后端架构', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (6, 'Apple', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (7, 'iOS', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (8, 'Geek', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (9, '游戏', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (10, '生活', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (11, 'Internet', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (12, '城市', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (13, '品牌', '2020-05-22 13:48:27', '2020-05-22 13:48:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (14, 'test4', '2020-05-23 01:53:31', '2020-05-23 02:12:27', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (15, 'test2', '2020-05-23 01:54:48', '2020-05-23 01:54:48', 0);
INSERT INTO flask_restful.root_topic (id, name, create_time, update_time, deleted) VALUES (16, 'test3', '2020-05-23 01:55:08', '2020-05-23 01:55:08', 0);
create table topic
(
    id            int auto_increment
        primary key,
    name          varchar(256)                         not null,
    root_topic_id int        default 0                 null,
    create_time   datetime   default CURRENT_TIMESTAMP null comment '创建时间',
    update_time   datetime   default CURRENT_TIMESTAMP null comment '更新时间',
    deleted       tinyint(1) default 0                 not null comment '该项目是否被删除',
    constraint topic_ibfk_1
        foreign key (root_topic_id) references root_topic (id)
);

create index root_topic_id
    on topic (root_topic_id);

INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (1, '问与答', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (2, '分享发现 ', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (3, '分享创造', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (4, '奇思妙想', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (5, '分享邀请码', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (6, '自言自语', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (7, '随想', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (8, '设计', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (9, 'Blog', 1, '2020-05-22 13:50:05', '2020-05-22 13:50:05', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (10, '机器学习', 2, '2020-05-22 13:53:00', '2020-05-22 13:53:00', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (11, '数学', 2, '2020-05-22 13:53:00', '2020-05-22 13:53:00', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (12, 'TensorFlow', 2, '2020-05-22 13:53:00', '2020-05-22 13:53:00', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (13, '自然语言处理', 2, '2020-05-22 13:53:00', '2020-05-22 13:53:00', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (14, 'CUDA', 2, '2020-05-22 13:53:00', '2020-05-22 13:53:00', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (15, 'Torch', 2, '2020-05-22 13:53:00', '2020-05-22 13:53:00', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (16, 'Core ML', 2, '2020-05-22 13:53:00', '2020-05-22 13:53:00', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (17, 'Keras', 2, '2020-05-22 13:53:01', '2020-05-22 13:53:01', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (18, 'Chrome', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (19, 'Vue.js', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (20, 'CSS', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (21, 'Firefox', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (22, 'React', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (23, 'Angular', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (24, 'Flutter', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (25, 'Edge', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (26, 'Web Dev', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (27, 'Ionic', 3, '2020-05-23 03:20:41', '2020-05-23 03:20:41', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (29, 'Python', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (30, 'PHP', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (31, 'Java', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (32, 'JavaScript', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (33, 'Node.js', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (34, 'Go', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (35, 'HTML', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (36, 'Swift', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (37, 'Ruby on Rails', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (38, '.NET', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (39, 'Ruby', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (40, 'C#', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (41, 'Rust', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (42, 'Kotlin', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (43, 'Lua', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (44, 'TypeScript', 4, '2020-05-23 03:23:04', '2020-05-23 03:23:04', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (45, '云计算', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (46, '服务器', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (47, 'MySQL', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (48, 'NGINX', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (49, 'Docker', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (50, '数据库', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (51, 'Django', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (52, 'MongoDB', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (53, 'Redis', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (54, 'DevOps', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (55, 'Tornado', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (56, 'Elasticsearch', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (57, 'LeanCloud', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (58, 'Kubernetes', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (59, 'Cloudflare', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (60, 'Timescale', 5, '2020-05-23 03:25:57', '2020-05-23 03:25:57', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (61, '二手交易', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (62, '酷工作', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (63, '职场话题', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (64, '求职', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (65, '天黑以后', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (66, '免费赠送', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (67, '音乐', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (68, '电影', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (69, '物物交换', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (70, '团购', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (71, '投资', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (72, '剧集', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (73, '信用卡', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (74, '旅行', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (75, '美酒与美食', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (76, '阅读', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (77, '摄影', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (78, '宠物', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (79, 'Baby', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (80, '绿茵场', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (81, '咖啡', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (82, '非诚勿扰', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (83, '日记', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (84, '骑行', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (85, '植物', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (86, '蘑菇 ', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
INSERT INTO flask_restful.topic (id, name, root_topic_id, create_time, update_time, deleted) VALUES (87, '行程控', 10, '2020-05-23 03:32:40', '2020-05-23 03:32:40', 0);
create table user
(
    id                           int auto_increment
        primary key,
    email                        varchar(100)                         not null,
    password_hash                varchar(256)                         not null comment '登陆密码 hash 之后的值',
    name                         varchar(100)                         null,
    phone                        varchar(20)                          null comment '电话号码',
    avatar                       varchar(256)                         null comment '用户头像',
    website                      varchar(100)                         null comment '个人网站',
    company                      varchar(100)                         null comment '所在公司',
    job                          varchar(100)                         null comment '职位',
    location                     varchar(100)                         null comment '所在地',
    signature                    varchar(256)                         null comment '签名',
    Dribbble                     varchar(256)                         null comment 'Dribbble',
    Duolingo                     varchar(256)                         null comment 'Duolingo',
    About_me                     varchar(256)                         null comment 'About.me',
    Last_me                      varchar(256)                         null comment 'Last.fm',
    Goodreads                    varchar(256)                         null comment 'Goodreads',
    GitHub                       varchar(256)                         null comment 'GitHub',
    PSN_ID                       varchar(256)                         null comment 'PSN ID',
    Steam_ID                     varchar(256)                         null comment 'Steam_ID',
    Twitch                       varchar(256)                         null comment 'Twitch',
    BattleTag                    varchar(256)                         null comment 'BattleTag',
    Instagram                    varchar(256)                         null comment 'Instagram',
    Telegram                     varchar(256)                         null comment 'Telegram',
    Twitter                      varchar(256)                         null comment 'Twitter',
    BTC_Address                  varchar(256)                         null comment 'BTC Address',
    Coding_net                   varchar(256)                         null comment 'Coding.net',
    Personal_Introduction        varchar(256)                         null comment '个人简介',
    state_update_view_permission int                                  null comment '状态更新查看权限',
    community_rich_rank          tinyint(1)                           null comment '社区财富排行榜',
    money                        int                                  null comment '余额',
    show_remain_money            tinyint(1)                           null comment '是否显示余额',
    use_avatar_for_favicon       tinyint(1)                           null comment '使用节点头像作为页面 favicon',
    use_high_resolution_avatar   tinyint(1)                           null comment '使用高精度头像',
    time_zone                    varchar(256)                         null comment '默认使用的时区',
    create_time                  datetime   default CURRENT_TIMESTAMP null comment '创建时间',
    update_time                  datetime   default CURRENT_TIMESTAMP null comment '更新时间',
    deleted                      tinyint(1) default 0                 not null comment '该项目是否被删除'
);

INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (1, 'hrui801@gmail.com', 'pbkdf2:sha256:150000$m8MrvhvY$7a8f18de5017062cafe68f7e3c663fd078b45c858f09f549265746fec02e6261', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:41:49', '2020-05-22 13:41:49', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (2, 'hrui802@gmail.com', 'pbkdf2:sha256:150000$AXBJQ4TL$e71bc1f85b6cb5a458214dcde55e95e9bd1d9ca28758ee4e99f1c221064b4f3e', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:41:56', '2020-05-22 13:41:56', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (3, 'hrui803@gmail.com', 'pbkdf2:sha256:150000$PSVB0MRc$b13aad76600960788a4e503b2e1abbe45fdcc47a285a9a4f3ffbd4230a89b08f', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:42:00', '2020-05-22 13:42:00', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (4, 'hrui804@gmail.com', 'pbkdf2:sha256:150000$cT7NI48J$4c6a17112862f0ddacd4d641d8aa55d1768eb44622683dd3ac787e38134e8000', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:42:03', '2020-05-22 13:42:03', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (5, 'hrui805@gmail.com', 'pbkdf2:sha256:150000$pwcS1E1O$4dfd29afba21fef61833ab1071e2dad5ad322133e8e189755a788bc8203bfe3b', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:42:07', '2020-05-22 13:42:07', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (6, 'hrui806@gmail.com', 'pbkdf2:sha256:150000$hfu5F2cU$5d02e205590649c0824c22e4976919ba70fa96b150526ba2f7a997b5f14a25cb', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:42:11', '2020-05-22 13:42:11', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (7, 'hrui807@gmail.com', 'pbkdf2:sha256:150000$jNvWqpHs$fb8dfa8cbd9dc83ff1f7479bea5738c36cce9cefa559d740c108fc3a2b009211', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:42:16', '2020-05-22 13:42:16', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (8, 'hrui808@gmail.com', 'pbkdf2:sha256:150000$TkWV3eUG$b92e1b9cc9dcb3df5900cf09fef5c782dd3ed171128dad7a66aba0e4790460b2', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:42:20', '2020-05-22 13:42:20', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (9, 'hrui809@gmail.com', 'pbkdf2:sha256:150000$7CNvv2XG$c9d01092175d823dc1b3f4e1aa16a5c20fd32ae451339726f8187b1a8bf59406', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:42:23', '2020-05-22 13:42:23', 0);
INSERT INTO flask_restful.user (id, email, password_hash, name, phone, avatar, website, company, job, location, signature, Dribbble, Duolingo, About_me, Last_me, Goodreads, GitHub, PSN_ID, Steam_ID, Twitch, BattleTag, Instagram, Telegram, Twitter, BTC_Address, Coding_net, Personal_Introduction, state_update_view_permission, community_rich_rank, money, show_remain_money, use_avatar_for_favicon, use_high_resolution_avatar, time_zone, create_time, update_time, deleted) VALUES (10, 'hrui810@gmail.com', 'pbkdf2:sha256:150000$zfFnQiUh$2382855a69d1b6585daa75e4278d9d176c58267ac67e9c7d40128df2176eea7a', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, 0, 'utc', '2020-05-22 13:42:27', '2020-05-22 13:42:27', 0);
