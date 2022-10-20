from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import User
from accounts.models import Account

class AccountsTest(APITestCase):

    def setUp(self):
        self.account = Account.objects.create_user(
            username='joe',
            email='joe124@gmail.com',
            password='top_secret'
        )

    def test_cannot_access_account_information_when_not_authenticated(self):
        response = self.client.get('/api/v1/accounts/')

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_access_account_information_when_authenticated(self):
        token = Token.objects.create(user=self.account)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get('/api/v1/accounts/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.account.username)
        self.assertContains(response, self.account.email)

