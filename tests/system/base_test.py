from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self):
        app.testing = True #All the time life we are in testing mode
        self.app = app.test_client
