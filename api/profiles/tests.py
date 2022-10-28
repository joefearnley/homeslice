from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from accounts.models import Account


class ProfileTestMixin(TestCase):
    def setUp(self):
        self.account = Account.objects.create_user(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='john.m.doe@gmail.com',
            password='top_secret'
        )

        self.other_account = Account.objects.create_user(
            username='janedoe',
            first_name='Jane',
            last_name='Dole',
            email='jane.m.doe@gmail.com',
            password='top_secret'
        )

    def authenticate_account(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


class ProfilesTest(APITestCase, ProfileTestMixin):
    def test_cannot_access_profile_information_when_not_authenticated(self):
        response = self.client.get('/api/v1/profiles/')

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_access_profile_when_authenticated(self):
        self.authenticate_account()

        response = self.client.get('/api/v1/profiles/')

        print(response)
        print(response.data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
