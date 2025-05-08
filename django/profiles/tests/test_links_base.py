from django.test import TestCase
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
        self.client.force_login(user=self.account)

    def create_link(self):
        self.link = Link.objects.create(
            profile=self.profile,
            url='https://www.twitter.com/johndoe123',
            title='Twitter'
        )
