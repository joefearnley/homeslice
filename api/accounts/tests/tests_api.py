from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from accounts.models import Account


class AccountTestMixin(TestCase):
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


class AccessAccountTest(APITestCase, AccountTestMixin):
    def test_cannot_access_account_information_when_not_authenticated(self):
        response = self.client.get('/api/v1/accounts/')

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_access_account_information_when_authenticated(self):
        self.authenticate_account()

        response = self.client.get('/api/v1/accounts/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.account.username)
        self.assertContains(response, self.account.email)


class UpdateAccountNameTest(APITestCase, AccountTestMixin):
    def test_cannot_update_account_when_not_authenticated(self):
        response = self.client.get('/api/v1/accounts/')

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_update_account_first_name(self):
        self.authenticate_account()

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
        self.authenticate_account()

        post_data = {
            'username': self.account.username,
            'last_name': 'Doh!',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_account = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_account.first_name, self.account.first_name)
        self.assertEqual(updated_account.last_name, post_data['last_name'])


class UpdateAccountEmailAddressTest(APITestCase, AccountTestMixin):
    def test_cannot_update_email_address_when_not_authenticated(self):
        post_data = {
            'username': self.account.username,
            'email': 'johnny.d.doe@gmail.com'
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_cannot_update_email_address_when_empty(self):
        self.authenticate_account()

        post_data = {
            'username': self.account.username,
            'email': '',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field may not be blank.')

    def test_cannot_update_email_address_when_not_unique(self):
        self.authenticate_account()

        other_users_email = self.other_account.email

        post_data = {
            'username': self.account.username,
            'email': other_users_email
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field must be unique.')

    def test_can_update_email_address(self):
        self.authenticate_account()

        post_data = {
            'username': self.account.username,
            'email': 'johnny.d.doe@gmail.com'
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_account = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_account.email, post_data['email'])


class UpdateAccountUsernameTest(APITestCase, AccountTestMixin):
    def test_cannot_update_username_when_not_authenticated(self):
        post_data = {
            'username': 'johnnydoe',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_update_username_when_not_given(self):
        self.authenticate_account()

        post_data = {
            'username': '',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field may not be blank.')

    def test_cannot_update_username_when_not_unique(self):
        self.authenticate_account()

        post_data = {
            'username': self.other_account.username,
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'A user with that username already exists.')

    def test_username_can_be_updated(self):
        self.authenticate_account()

        post_data = {
            'username': 'johnnydoe',
        }

        response = self.client.patch('/api/v1/accounts/%s/' % self.account.id, post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_account = Account.objects.get(username=post_data['username'])
        self.assertEqual(updated_account.username, post_data['username'])


class AccountUpdatePasswordTest(APITestCase, AccountTestMixin):
    def test_cannot_update_password_when_not_authenticated(self):
        post_data = {
            'password': 'secrect_1243',
            'confirm_password': 'secrect_1243'
        }
        response = self.client.patch(reverse('update-password'), post_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_update_password_with_missing_fields(self):
        self.authenticate_account()

        post_data = {}

        response = self.client.patch(reverse('update-password'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], 'This field is required.')
        self.assertEqual(response.data['confirm_password'][0], 'This field is required.')

    def test_cannot_update_password_with_black_fields(self):
        self.authenticate_account()

        post_data = {
            'password': '',
            'confirm_password': '',
        }

        response = self.client.patch(reverse('update-password'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], 'This field may not be blank.')
        self.assertEqual(response.data['confirm_password'][0], 'This field may not be blank.')

    def test_cannot_update_password_when_too_short_common_numeric(self):
        self.authenticate_account()

        post_data = {
            'password': '1',
            'confirm_password': '1',
        }

        response = self.client.patch(reverse('update-password'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], 'This password is too short. It must contain at least 8 characters.')
        self.assertEqual(response.data['non_field_errors'][1], 'This password is too common.')
        self.assertEqual(response.data['non_field_errors'][2], 'This password is entirely numeric.')

    def test_cannot_update_password_when_do_not_match(self):
        self.authenticate_account()

        post_data = {
            'password': 'top_secret_123',
            'confirm_password': 'top_secret_1234',
        }

        response = self.client.patch(reverse('update-password'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['confirm_password'][0], 'The two password fields did not match.')


    def test_can_update_password(self):
        self.authenticate_account()

        new_password = 'top_secret_123'
        post_data = {
            'password': new_password,
            'confirm_password': new_password,
        }

        response = self.client.patch(reverse('update-password'), post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_account = Account.objects.get(username=self.account.username)
        self.assertEquals(updated_account.check_password(new_password), True)
