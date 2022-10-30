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


class AccessLinksTest(APITestCase, LinkTestMixin):
    def test_cannot_access_link_information_when_not_authenticated(self):
        response = self.client.get('/api/v1/links/')

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_access_links_when_authenticated(self):
        self.authenticate_account()

        response = self.client.get('/api/v1/links/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_can_view_links_data(self):
        self.authenticate_account()

        link = Link.objects.create(
            profile=self.profile,
            url='https://www.twitter.com/johndoe123',
            title='Twitter'
        )

        response = self.client.get('/api/v1/links/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, link.url)
        self.assertContains(response, link.title)

    def test_can_only_view_links_data_for_authenticated_account(self):
        self.authenticate_account()

        link = Link.objects.create(
            profile=self.profile,
            url='https://www.twitter.com/johndoe123',
            title='Twitter'
        )

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
        self.assertContains(response, link.url)
        self.assertContains(response, link.title)

        self.assertNotContains(response, other_link.url)
        self.assertNotContains(response, other_link.title)

