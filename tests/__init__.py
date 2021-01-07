import base64
from unittest import TestCase

from flask.testing import FlaskClient
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash

from app import create_app
from configures import settings
from models.orm import db

email = "hrui8005@gmail.com"
password = "11Aa*%$#"
password_hash = generate_password_hash(password)

auth_str = f"{email}:{password}"
headers = {"Authorization": "Basic " + base64.b64encode(bytes(auth_str, "ascii")).decode("ascii")}


class TestClient(FlaskClient):
    def open(self, *args, **kwargs):
        kwargs["headers"] = headers
        return super().open(*args, **kwargs)


class BaseTestCase(TestCase):
    client: FlaskClient

    @classmethod
    def setUpClass(cls) -> None:
        cls.engine = create_engine(settings.TEST_SQLALCHEMY_DATABASE)
        cls.engine.execute("DROP DATABASE  IF EXISTS %s;" % settings.TEST_DATABASE)
        cls.engine.execute("CREATE DATABASE IF NOT EXISTS %s;" % settings.TEST_DATABASE)

        cls.maxDiff = None
        cls.app = create_app()
        cls.app.config["SQLALCHEMY_DATABASE_URI"] = settings.TEST_SQLALCHEMY_DATABASE_URI
        cls.app.config["TESTING"] = True

        db.init_app(cls.app)
        with cls.app.app_context():
            db.create_all()
        cls.app.test_client_class = TestClient
        cls.client = cls.app.test_client()

        cls.engine.execute(
            f"INSERT INTO TEST.user (email, password_hash) VALUES ('{email}', '{password_hash}');"
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.app = create_app()
        cls.app.config["SQLALCHEMY_DATABASE_URI"] = settings.TEST_SQLALCHEMY_DATABASE_URI
        cls.app.config["TESTING"] = True
        db.init_app(cls.app)
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()
