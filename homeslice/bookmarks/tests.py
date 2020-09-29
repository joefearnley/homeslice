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

    def test_bookmarks_list_redirects_not_authenticated(self):
        response = self.client.get('/bookmarks/')

        self.assertRedirects(response, '/login/?next=/bookmarks/', 302)

    def test_bookmarks_list_renders_with_no_bookmarks(self):
        self.client.force_login(self.user)

        response = self.client.get('/bookmarks/')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        self.assertContains(response, 'No bookmarks yet!')
        self.assertContains(response, 'Add one!')
