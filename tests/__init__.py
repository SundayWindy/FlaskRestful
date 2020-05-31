import base64
from unittest import TestCase

from flask.testing import FlaskClient
from sqlalchemy import create_engine

from app import create_app
from configures import settings
from models.database_models import db

auth_str = "hrui8005@gmail.com:11Aa*%$#"
headers = {'Authorization': 'Basic ' + base64.b64encode(bytes(auth_str, 'ascii')).decode('ascii')}


class TestClient(FlaskClient):
    def open(self, *args, **kwargs):
        kwargs['headers'] = headers
        return super().open(*args, **kwargs)


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.engine = create_engine(settings.TEST_SQLALCHEMY_DATABASE)
        cls.engine.execute("DROP DATABASE  IF EXISTS %s;" % settings.TEST_DATABASE)
        cls.engine.execute("CREATE DATABASE IF NOT EXISTS %s;" % settings.TEST_DATABASE)

    def setUp(self):
        self.maxDiff = None
        self.app = create_app()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = settings.TEST_SQLALCHEMY_DATABASE_URI
        self.app.config['TESTING'] = True

        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
        self.app.test_client_class = TestClient
        self.client = self.app.test_client()

        self.user1 = {"email": "hrui8005@gmail.com", "password": "11Aa*%$#"}
        self.client.post("/api/users", json=self.user1)

    def tearDown(self) -> None:
        self.app = create_app()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = settings.TEST_SQLALCHEMY_DATABASE_URI
        self.app.config['TESTING'] = True
        db.init_app(self.app)
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
