NAMESPACE = "PRODUCTION"
date_format = "%Y-%m-%d %H:%M:%S"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ROOT@mysql/flask_restful?charset=UTF8MB4"
SQLALCHEMY_DATABASE_BASE = "mysql+pymysql://root:ROOT@mysql/"
SQLALCHEMY_TRACK_MODIFICATIONS = False

TEST_SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/TEST?charset=UTF8MB4"
TEST_DATABASE = "TEST"
