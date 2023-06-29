import os

NAMESPACE = os.environ.get('NAMESPACE', 'PRODUCTION')
SECRET_KEY = os.environ.get('SECRET_KEY', 'fbca22c2a2ed11ea91b488e9fe4e9d33')
date_format = '%Y-%m-%d %H:%M:%S'
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:ROOT@mysql/flask_restful?charset=UTF8MB4'
)
SQLALCHEMY_DATABASE_BASE = os.environ.get('SQLALCHEMY_DATABASE_BASE', 'mysql+pymysql://root:ROOT@mysql/')
SQLALCHEMY_TRACK_MODIFICATIONS = False

TEST_SQLALCHEMY_DATABASE = os.environ.get('TEST_SQLALCHEMY_DATABASE', 'mysql+pymysql://root:@localhost/')
TEST_SQLALCHEMY_DATABASE_URI = os.environ.get(
    'TEST_SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:@localhost/TEST?charset=UTF8MB4'
)
TEST_DATABASE = os.environ.get('TEST_DATABASE', 'TEST')

LOCAL_SQLALCHEMY_DATABASE_URI = os.environ.get(
    'LOCAL_SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:ROOT@localhost:3307/flask_restful?charset=UTF8MB4'
)
LOCAL_SQLALCHEMY_DATABASE_BASE = os.environ.get(
    'LOCAL_SQLALCHEMY_DATABASE_BASE', 'mysql+pymysql://root:ROOT@localhost:3307/'
)
