import unittest
import urllib2

from flask_testing import LiveServerTestCase
from selenium import webdriver

from app import create_app, db
from app.models import Location

class TestBase(LiveServerTestCase):
	"""This is base handler for rest of the tests cases """
	def create_app(self):
		""" setup app context """
		config_name = 'testing'
		app = create_app(config_name)
		return app

	def setUp(self):
		""" Runs before each test"""
		self.driver = webdriver.Chrome()
		self.driver.get(self.get_server_url())

		db.session.commit()
		db.drop_all()
		db.create_all()

		# create a test location
		self.loc = Location(lat = 34.34, lng = 65.45, address = "could be anywhere, who knows")

		# save
		db.session.add(self.loc)
		db.session.commit()

	def tearDown(self):
		"""Runs after every test case """
		self.driver.quit()

	def test_server_is_up_and_running(self):
		response = urllib2.urlopen(self.get_server_url())
		self.assertEqual(response.code, 200)

class ClassName(TestBase):
	"""Testing map click events"""
	def test_valid_map_clicks(self):
		"""
		clicks on maps element at specific coordinates, use screen offset for that.
		Verify if database get incremented
		"""
		pass


if __name__ == '__main__':
	unittest.run()
