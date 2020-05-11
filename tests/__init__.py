from unittest import TestCase
from sqlalchemy import create_engine

from configures import settings


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


class BaseApiTestCase(BaseTestCase):

	def setUp(self):
		self.maxDiff = None
		# self.clear_context()
		from app import create_app
		self.app = create_app()
		self.client = self.app.test_client()

# self.init_db()

# def tearDown(self):
# 	self.drop_db()
# 	del self.app.socrates
