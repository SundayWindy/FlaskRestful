from unittest import TestCase
from sqlalchemy import create_engine

from app import create_app
from configures import settings
from models.database_model import db


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.engine = create_engine(settings.SQLALCHEMY_DATABASE_BASE)
        cls.engine.execute("DROP DATABASE  IF EXISTS  %s" % settings.TEST_DATABASE)
        cls.engine.execute("CREATE DATABASE IF NOT EXISTS %s" % settings.TEST_DATABASE)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.engine = create_engine(settings.SQLALCHEMY_DATABASE_BASE)
        cls.engine.execute("drop database %s" % settings.TEST_DATABASE)

    def setUp(self):
        self.maxDiff = None
        self.app = create_app()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = settings.TEST_SQLALCHEMY_DATABASE_URI
        self.app.config['TESTING'] = True

        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        self.app = create_app()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = settings.TEST_SQLALCHEMY_DATABASE_URI
        self.app.config['TESTING'] = True
        db.init_app(self.app)
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
