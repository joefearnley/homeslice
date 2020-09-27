from django.test import TestCase, Client
from django.contrib.auth.models import User


class BookmarksTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='joe',
            email='joe124@gmail.com',
            password='top_secret'
        )

    def test_bookmarks_page_renders(self):
        response = self.client.get('/bookmarks/')

        self.assertEqual(response.status_code, 200)
