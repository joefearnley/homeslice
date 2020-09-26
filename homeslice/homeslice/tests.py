import unittest
from django.test import Client

class HomepageTest(unittest.TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_homepage_renders(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
