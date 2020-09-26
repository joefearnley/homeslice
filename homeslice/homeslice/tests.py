import unittest
from django.test import Client, SimpleTestCase


class HomepageTest(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_renders(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Homeslice - your bookmarking buddy.')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Register')
