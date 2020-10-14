from django.test import TestCase, Client


class HomepageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_renders(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Homeslice - your bookmarking buddy.')

    def test_homepage_shows_login_register_links(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Log in')
        self.assertContains(response, 'Sign up')
