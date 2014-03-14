#!/usr/bin/env python
# encoding: utf-8

from google.appengine.ext import testbed
import unittest2
import tempfile
import main

class AppTest(unittest2.TestCase):

	def setUp(self):
		main.app.config['TESTING'] = True
		self.app = main.app.test_client()
		self.testbed = testbed.Testbed()
		self.testbed.activate()
		main.app.init_db()

	def tearDown(self):
		self.testbed.deactivate()

	def testHome(self):
		rv = self.app.get('/')
		self.assertTrue(rv.status == '200 OK')

if __name__ == '__main__':
	unittest2.main()