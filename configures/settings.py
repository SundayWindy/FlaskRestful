NAMESPACE = "PRODUCTION"
SECRET_KEY = "fbca22c2a2ed11ea91b488e9fe4e9d33"
date_format = "%Y-%m-%d %H:%M:%S"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@mysql/flask_restful?charset=UTF8MB4"
SQLALCHEMY_DATABASE_BASE = "mysql+pymysql://root:@mysql/"
SQLALCHEMY_TRACK_MODIFICATIONS = False

TEST_SQLALCHEMY_DATABASE = "mysql+pymysql://root:@localhost/"
TEST_SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/TEST?charset=UTF8MB4"
TEST_DATABASE = "TEST"
