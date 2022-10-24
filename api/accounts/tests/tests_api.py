from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import User
from accounts.models import Account


class AccessAccountTest(APITestCase):

    def setUp(self):
        self.account = Account.objects.create_user(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='john.m.doe@gmail.com',
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


class UpdateAccountTest(APITestCase):

    def setUp(self):
        self.account = Account.objects.create_user(
           username='johndoe',
            first_name='John',
            last_name='Doe',
            email='john.m.doe@gmail.com',
            password='top_secret'
        )

    def test_cannot_update_account_when_not_authenticated(self):
        response = self.client.get('/api/v1/accounts/')

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_update_account_first_name(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': self.account.username,
            'first_name': 'Jane',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_user = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_user.first_name, post_data['first_name'])
        self.assertEqual(updated_user.last_name, self.account.last_name)

    def test_can_update_account_last_name(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': self.account.username,
            'last_name': 'Dole',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_user = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_user.first_name, self.account.first_name)
        self.assertEqual(updated_user.last_name, post_data['last_name'])


    def test_cannot_update_account_email_address_when_empty(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': self.account.username,
            'email': '',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_user = Account.objects.get(username=post_data['username'])

        print(updated_user.email)

        # self.assertEqual(updated_user.first_name, self.account.first_name)
        # self.assertEqual(updated_user.last_name, post_data['last_name'])

    # update email address
    #  validation
    #       [ ] not empty
    #       [ ] valid email
    #       [ ] email not already i user

    # update username
    #  validation
    #       not empty
    #       not already in use

    # update password
    #  validation
    #    not empty
    #    at least 8 characters
    #    confirmation matches
