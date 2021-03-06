from django.test import TestCase, Client
from django.contrib.auth.models import User
from bookmarks.models import Bookmark
from bookmarks.forms import BookmarkForm


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

    def test_bookmarks_list_shows_users_bookmarks(self):
        bookmark1 = Bookmark.objects.create(
            user=self.user,
            name='Bookmark 1',
            url='https://www.google.com',
        )

        bookmark2 = Bookmark.objects.create(
            user=self.user,
            name='Bookmark 2',
            url='https://www.yahoo.com',
        )

        self.client.force_login(self.user)

        response = self.client.get('/bookmarks/')

        self.assertEquals(response.status_code, 200)

        self.assertContains(response, 'Bookmark 1')
        self.assertContains(response, 'https://www.google.com')
        self.assertContains(response, 'Bookmark 2')
        self.assertContains(response, 'https://www.yahoo.com')


    def test_bookmarks_list_shows_users_bookmarks_only(self):
        ''' set up bookmarks for multiple users - main users should not 
            see those that belong to the second users '''

        user1 = User.objects.create_user(
            username='user1',
            email='user1_123@gmail.com',
            password='top_secret'
        )

        user2 = User.objects.create_user(
            username='user2',
            email='user2_123@gmail.com',
            password='top_secret'
        )

        bookmark1 = Bookmark.objects.create(
            user=user1,
            name='Bookmark 1',
            url='https://www.google.com',
        )

        bookmark2 = Bookmark.objects.create(
            user=user1,
            name='Bookmark 2',
            url='https://www.yahoo.com',
        )

        bookmark3 = Bookmark.objects.create(
            user=user2,
            name='Bookmark 3',
            url='https://www.bing.com',
        )

        self.client.force_login(user1)

        response = self.client.get('/bookmarks/')

        self.assertEquals(response.status_code, 200)

        self.assertContains(response, 'Bookmark 1')
        self.assertContains(response, 'https://www.google.com')

        self.assertNotContains(response, 'Bookmark 3')
        self.assertNotContains(response, 'https://www.bing.com')


    def test_bookmarks_list_shows_notes(self):
        bookmark1 = Bookmark.objects.create(
            user=self.user,
            name = 'Bookmark 1',
            url = 'https://www.google.com',
            notes='This is the first note.',
        )

        bookmark2 = Bookmark.objects.create(
            user=self.user,
            name='Bookmark 2',
            url='https://www.yahoo.com',
            notes='This is the second note.',
        )

        self.client.force_login(self.user)

        response = self.client.get('/bookmarks/')

        self.assertEquals(response.status_code, 200)

        self.assertContains(response, 'This is the first note.')
        self.assertContains(response, 'This is the second note.')


class BookmarksCreateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='joe',
            email='joe124@gmail.com',
            password='top_secret'
        )


    def test_add_bookmark_uses_form_template(self):
        self.client.force_login(self.user)

        response = self.client.get('/bookmarks/add')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_update.html')

    def test_cannot_create_bookmark_with_no_name(self):
        self.client.force_login(self.user)

        form_data = {
            'name': '',
            'url': 'https://www.google.com',
            'notes': '',
        }

        response = self.client.post('/bookmarks/add', data=form_data)
        self.assertContains(response, 'Please enter a name')

    def test_cannot_create_bookmark_with_no_url(self):
        self.client.force_login(self.user)

        form_data = {
            'name': 'Bookmark 1',
            'url': '',
            'notes': '',
        }

        response = self.client.post('/bookmarks/add', data=form_data)
        self.assertContains(response, 'Please enter a valid URL')

    def test_can_create_bookmark(self):
        self.client.force_login(self.user)

        form_data = {
            'name': 'Bookmark 1',
            'url': 'https://www.google.com',
            'notes': 'This is the first note.',
        }

        response = self.client.post('/bookmarks/add', data=form_data)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/bookmarks/')

        bookmark = Bookmark.objects.latest('created_date')

        self.assertEquals(form_data['name'], bookmark.name)
        self.assertEquals(form_data['url'], bookmark.url)
        self.assertEquals(form_data['notes'], bookmark.notes)

class BookmarksUpdateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='joe',
            email='joe124@gmail.com',
            password='top_secret'
        )

        self.bookmark = Bookmark(
            user=self.user,
            name='Bookmark 1',
            url='https://www.google.com',
            notes='This is the first note.',
        )

        self.bookmark.save()

    def test_edit_bookmark_uses_form_template(self):
        self.client.force_login(self.user)

        update_url = "/bookmarks/edit/%s" % self.bookmark.id
        response = self.client.get(update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_update.html')

    def test_cannot_update_bookmark_with_no_name(self):
        self.client.force_login(self.user)

        form_data = {
            'name': '',
            'url': 'https://www.google.com',
            'notes': '',
        }

        update_url = "/bookmarks/edit/%s" % self.bookmark.id
        response = self.client.post(update_url, data=form_data)
        self.assertContains(response, 'Please enter a name')

    def test_cannot_update_bookmark_with_no_url(self):
        self.client.force_login(self.user)

        form_data = {
            'name': 'Bookmark 1',
            'url': '',
            'notes': '',
        }

        update_url = "/bookmarks/edit/%s" % self.bookmark.id
        response = self.client.post(update_url, data=form_data)
        self.assertContains(response, 'Please enter a valid URL')

    def test_can_update_bookmark(self):
        bookmark = Bookmark(
            user=self.user,
            name='Bookmark 1',
            url='https://www.google.com',
            notes='This is the first note.',
        )

        bookmark.save()

        form_data = {
            'name': 'Bookmark 8',
            'url': 'https://www.google123.com',
            'notes': 'This is the first note.',
        }

        self.client.force_login(self.user)

        update_url = "/bookmarks/edit/%s" % bookmark.id
        response = self.client.post(update_url, data=form_data)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/bookmarks/')

        bookmark.refresh_from_db()

        self.assertEquals(form_data['name'], bookmark.name)
        self.assertEquals(form_data['url'], bookmark.url)
        self.assertEquals(form_data['notes'], bookmark.notes)


class BookmarksDeleteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='joe',
            email='joe124@gmail.com',
            password='top_secret'
        )

        self.bookmark = Bookmark(
            user=self.user,
            name='Bookmark 1',
            url='https://www.google.com',
            notes='This is the first note.',
        )

        self.bookmark.save()

    def test_can_see_delete_bookmark_form(self):
        self.client.force_login(self.user)

        delete_url = "/bookmarks/delete/%s" % self.bookmark.id
        response = self.client.get(delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html')


class BookmarkFormTest(TestCase):
    def test_form_does_not_validate_with_empty_data(self):
        form_data = {
            'name': '',
            'url': '',
            'notes': '',
        }

        form = BookmarkForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_does_not_validate_with_no_name(self):
        form_data = {
            'name': '',
            'url': 'https://www.google.com',
        }

        form = BookmarkForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_does_not_validate_with_no_url(self):
        form_data = {
            'name': '',
            'url': 'https://www.google.com',
        }

        form = BookmarkForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_validates(self):
        form_data = {
            'name': 'Bookmark 1',
            'url': 'https://www.google.com',
            'notes': 'This is the first note.',
        }

        form = BookmarkForm(data=form_data)
        self.assertTrue(form.is_valid())
