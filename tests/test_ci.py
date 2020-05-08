from unittest import TestCase


class T(TestCase):
	def test_ci_work(self):
		import  handlers
		from exceptions.exceptions import InvalidArgumentException
		self.assertEqual(1, 1)
