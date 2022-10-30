from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from accounts.models import Account
from profiles.models import Profile


class LinkTestMixin(TestCase):
    def setUp(self):
        self.account = Account.objects.create_user(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='john.m.doe@gmail.com',
            password='top_secret'
        )

    def authenticate_account(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def create_profile(self):
        self.profile = Profile.objects.create(
            account=self.account,
            title='The John Doe Home Page',
            bio='this is a little somthing about me'
        )