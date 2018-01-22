import os
import unittest
from flask_testing import TestCase

from app import create_app, db
from app.models import Location


class TestBase(TestCase):
	"""docstring for TestBase"""

	def create_app(self):

		# test configuration 
		config_name = 'testing'
		app = create_app(config_name)
		
		return app

	def setUP(self):
		"""
		To be automatically executed before each test 
		"""
		db.create_all()

		loc = Location(lat = 4.53, lng = 54.3, address = "adfalskdfaslkjdf")
		db.session.add(loc)
		db.sessoin.commit()

	def tearDown(self):
		"""
		To be automatically executed after each test
		"""
		db.session.remove()
		db.drop_all()


class TestModels(TestBase):
	"""docstring for TestModels"""
	def test_location_model(self):
		"""
		Test number of records in Location Table
		"""
		self.assertEqual(Location.query.count(), 1)

if __name__ == '__main__':
	unittest.main()

