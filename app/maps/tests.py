import os
import unittest
from flask_testing import TestCase
from flask import url_for, abort

from app import create_app, db
from app.models import Location


class TestBase(TestCase):
	"""docstring for TestBase"""
	# SQLALCHEMY_DATABASE_URI = "sqlite://"
	# TESTING = True
	def create_app(self):

		config_name = 'testing'
		app = create_app(config_name)
		return app


	def setUp(self):
		"""
		To be automatically executed before each test 
		"""
		db.create_all()

		loc = Location(lat = 4.53, lng = 54.3, address = "adfalskdfaslkjdf")
		
		db.session.add(loc)
		db.session.commit()

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

# 	def test_lat_type(self):
# 		"""
# 		Test lat type
# 		"""
# 		loc = db.session.query().first()
# 		self.assertEqual(type(loc.lat), float)

# 	def test_lng_type(self):
# 		"""
# 		Test lat type
# 		"""
# 		loc = db.session.query().first()
# 		self.assertEqual(type(loc.lng), float)

# 	def test_address_type(self):
# 		"""
# 		Test lat type
# 		"""
# 		loc = db.session.query().first()
# 		self.assertEqual(type(loc.address), str)

# 	def test_address_length_sanity(self):
# 		"""
# 		check if max lenght is smaller than threshold
# 		"""
# 		loc = db.session.query().first()
# 		self.assertL


# class TestViews(TestBase):
# 	"""docstring for TestViews"""

# 	def test_home_page_get(self):
# 		"""
# 		Test if home page is accessible by get
# 		"""
# 		response = self.client.get(url_for('maps.homepage'))
#         self.assertEqual(response.status_code, 200)

#     def test_home_page_post(self):
# 		"""
# 		Test if home page is accessible by post
# 		"""
# 		response = self.client.post(url_for('maps.homepage'))
#         self.assertEqual(response.status_code, 200)

#     def test_fetch_page(self):
#     	"""
# 		Test if fetch page is accessible
#     	"""
#     	response = self.client.get(url_for('maps.fetch'))
#         self.assertEqual(response.status_code, 200)

#     def test_clear_page(self):

#     	"""
#     	Test if clear page is accessible
#     	"""
#     	response = self.client.get(url_for('maps.clear'))
#         self.assertEqual(response.status_code, 200)
	

if __name__ == '__main__':
	unittest.main()

