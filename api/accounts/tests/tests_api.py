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


class UpdateAccountNameTest(APITestCase):

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
            'first_name': 'Johnny',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_account = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_account.first_name, post_data['first_name'])
        self.assertEqual(updated_account.last_name, self.account.last_name)

    def test_can_update_account_last_name(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': self.account.username,
            'last_name': 'Doh!',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_account = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_account.first_name, self.account.first_name)
        self.assertEqual(updated_account.last_name, post_data['last_name'])


class UpdateAccountEmailAddressTest(APITestCase):
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

    def test_cannot_update_email_address_when_empty(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': self.account.username,
            'email': '',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field may not be blank.')

    def test_cannot_update_email_address_when_not_unique(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        other_users_email = self.other_account.email

        post_data = {
            'username': self.account.username,
            'email': other_users_email
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field must be unique.')

    def test_can_update_email_address(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': self.account.username,
            'email': 'johnny.d.doe@gmail.com'
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_account = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_account.email, post_data['email'])


class UpdateAccountUsernameTest(APITestCase):
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

    def test_cannot_update_username_when_not_given(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': '',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field may not be blank.')

    def test_cannot_update_username_when_not_unique(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': self.other_account.username,
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'A user with that username already exists.')

    def test_username_can_be_updated(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        post_data = {
            'username': 'johnnydoe',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_account = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_account.username, post_data['username'])

    # update password
    #  validation
    #    not empty
    #    at least 8 characters
    #    confirmation matches
