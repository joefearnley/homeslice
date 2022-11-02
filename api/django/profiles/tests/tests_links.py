from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from accounts.models import Account
from profiles.models import Profile, Link


class LinkTestMixin(TestCase):
    def setUp(self):
        self.account = Account.objects.create_user(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='john.m.doe@gmail.com',
            password='top_secret'
        )

        self.profile = Profile.objects.create(
            account=self.account,
            title='The John Doe Home Page',
            bio='this is a little somthing about me'
        )

    def authenticate_account(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def create_link(self):
        self.link = Link.objects.create(
            profile=self.profile,
            url='https://www.twitter.com/johndoe123',
            title='Twitter'
        )


class AccessLinksTest(APITestCase, LinkTestMixin):
    def test_cannot_access_link_information_when_not_authenticated(self):
        response = self.client.get('/api/v1/links/')

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_access_links_when_authenticated(self):
        self.authenticate_account()

        response = self.client.get('/api/v1/links/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_can_only_view_links_data_for_authenticated_account(self):
        self.authenticate_account()
        self.create_link()

        other_account = Account.objects.create_user(
            username='janedoe',
            first_name='Jane',
            last_name='Doe',
            email='jane.b.doe@gmail.com',
            password='top_secret'
        )

        other_profile = Profile.objects.create(
            account=other_account,
            title='The Jane Doe Home Page',
            bio='this is a little somthing about me (the jane doe)'
        )

        other_link = Link.objects.create(
            profile=other_profile,
            url='https://www.instagram.com/janedoe456',
            title='Jane Doe Instagram'
        )

        response = self.client.get('/api/v1/links/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.link.url)
        self.assertContains(response, self.link.title)

        self.assertNotContains(response, other_link.url)
        self.assertNotContains(response, other_link.title)

    def test_can_view_links_data(self):
        self.authenticate_account()
        self.create_link()

        response = self.client.get('/api/v1/links/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.link.url)
        self.assertContains(response, self.link.title)


class CreateLinksTest(APITestCase, LinkTestMixin):
    def test_cannot_create_link_when_not_authenticated(self):
        post_data = {
            'url': 'https://instagram.com/jdoe1234',
            'title': 'Instagram Account'
        }

        response = self.client.get('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_create_link_when_no_data_is_provided(self):
        self.authenticate_account()

        post_data = {}

        response = self.client.post('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'This field is required.')
        self.assertEqual(response.data['title'][0], 'This field is required.')

    def test_cannot_create_link_when_data_is_empty(self):
        self.authenticate_account()

        post_data = {
            'url': '',
            'title': ''
        }

        response = self.client.post('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'This field may not be blank.')
        self.assertEqual(response.data['title'][0], 'This field may not be blank.')

    def test_cannot_create_link_when_no_url_is_provided(self):
        self.authenticate_account()

        post_data = {
            'title': 'Instagram Account'
        }

        response = self.client.post('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'This field is required.')

    def test_cannot_create_link_when_url_is_blank(self):
        self.authenticate_account()

        post_data = {
            'url': '',
            'title': 'Instagram Account'
        }

        response = self.client.post('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'This field may not be blank.')

    def test_cannot_create_link_when_no_title_is_provided(self):
        self.authenticate_account()

        post_data = {
            'url': 'https://instagram.com/jdoe1234',
        }

        response = self.client.post('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0], 'This field is required.')

    def test_cannot_create_link_when_title_is_blank(self):
        self.authenticate_account()

        post_data = {
            'url': 'https://instagram.com/jdoe1234',
            'title': ''
        }

        response = self.client.post('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0], 'This field may not be blank.')

    def test_can_create_link(self):
        self.authenticate_account()

        post_data = {
            'url': 'https://instagram.com/jdoe1234',
            'title': 'Instagram Account'
        }

        response = self.client.post('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        link = Link.objects.filter(profile=self.profile).first()
        self.assertEqual(link.url, post_data['url'])
        self.assertEqual(link.title, post_data['title'])


class UpdateLinksTest(APITestCase, LinkTestMixin):
    def test_cannot_update_link_when_not_authenticated(self):
        post_data = {
            'url': 'https://instagram.com/jdoe1234',
            'title': 'Instagram Account'
        }

        response = self.client.get('/api/v1/links/', post_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_update_link_when_no_data_is_provided(self):
        self.authenticate_account()
        self.create_link()

        post_data = {}

        response = self.client.put('/api/v1/links/%s/' % self.link.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'This field is required.')
        self.assertEqual(response.data['title'][0], 'This field is required.')

    def test_cannot_update_link_when_data_is_blank(self):
        self.authenticate_account()
        self.create_link()

        post_data = {
            'url': '',
            'title': ''
        }

        response = self.client.put('/api/v1/links/%s/' % self.link.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'This field may not be blank.')
        self.assertEqual(response.data['title'][0], 'This field may not be blank.')

    def test_cannot_update_link_when_url_is_not_provided(self):
        self.authenticate_account()
        self.create_link()

        post_data = {
            'title': 'Instagram'
        }

        response = self.client.put('/api/v1/links/%s/' % self.link.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'This field is required.')

    def test_cannot_update_link_when_url_is_blank(self):
        self.authenticate_account()
        self.create_link()

        post_data = {
            'url': '',
            'title': 'Instagram'
        }

        response = self.client.put('/api/v1/links/%s/' % self.link.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'This field may not be blank.')

    def test_cannot_update_link_when_title_is_not_provided(self):
        self.authenticate_account()
        self.create_link()

        post_data = {
            'url': 'https://instagram.com/jdoe1234'
        }

        response = self.client.put('/api/v1/links/%s/' % self.link.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0], 'This field is required.')

    def test_cannot_update_link_when_url_is_blank(self):
        self.authenticate_account()
        self.create_link()

        post_data = {
            'url': 'https://instagram.com/jdoe1234',
            'title': ''
        }

        response = self.client.put('/api/v1/links/%s/' % self.link.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0], 'This field may not be blank.')

    def test_can_only_update_links_for_authenticated_account(self):
        self.authenticate_account()
        self.create_link()

        other_account = Account.objects.create_user(
            username='janedoe',
            first_name='Jane',
            last_name='Doe',
            email='jane.b.doe@gmail.com',
            password='top_secret'
        )

        other_profile = Profile.objects.create(
            account=other_account,
            title='The Jane Doe Home Page',
            bio='this is a little somthing about me (the jane doe)'
        )

        other_link = Link.objects.create(
            profile=other_profile,
            url='https://www.instagram.com/janedoe456',
            title='Jane Doe Instagram'
        )

        post_data = {
            'url': 'https://instagram.com/jdoe1234',
            'title': 'Instagram Account'
        }

        response = self.client.put('/api/v1/links/%s/' % other_link.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_update_link(self):
        self.authenticate_account()
        self.create_link()

        post_data = {
            'url': 'https://instagram.com/jdoe1234',
            'title': 'Instagram Account'
        }

        response = self.client.put('/api/v1/links/%s/' % self.link.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_link = Link.objects.get(id=self.link.id)
        self.assertEqual(updated_link.url, post_data['url'])
        self.assertEqual(updated_link.title, post_data['title'])


class DeleteLinkTest(APITestCase, LinkTestMixin):
    def test_cannot_delete_link_when_not_authenticated(self):
        self.create_link()

        response = self.client.delete('/api/v1/links/%s/' % self.link.id)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_only_delete_links_for_authenticated_account(self):
        self.authenticate_account()
        self.create_link()

        other_account = Account.objects.create_user(
            username='janedoe',
            first_name='Jane',
            last_name='Doe',
            email='jane.b.doe@gmail.com',
            password='top_secret'
        )

        other_profile = Profile.objects.create(
            account=other_account,
            title='The Jane Doe Home Page',
            bio='this is a little somthing about me (the jane doe)'
        )

        other_link = Link.objects.create(
            profile=other_profile,
            url='https://www.instagram.com/janedoe456',
            title='Jane Doe Instagram'
        )

        response = self.client.delete('/api/v1/links/%s/' % other_link.id)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_delete_links(self):
        self.authenticate_account()
        self.create_link()

        response = self.client.delete('/api/v1/links/%s/' % self.link.id)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        deleted_link = Link.objects.filter(id=self.link.id)
        self.assertEquals(0, len(deleted_link))
