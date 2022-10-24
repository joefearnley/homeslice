from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import User
from accounts.models import Account


class SignUpTest(APITestCase):
    def test_cannot_signup_for_an_account_with_no_data(self):
        response = self.client.post('/api/v1/signup/')

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field is required.')
        self.assertEqual(response.data['email'][0], 'This field is required.')
        self.assertEqual(response.data['password'][0], 'This field is required.')

    def test_cannot_signup_for_an_account_with_no_username(self):
        post_data = {
            'email': 'john.m.doe@gmail.com',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field is required.')

    def test_cannot_signup_for_an_account_when_username_is_blank(self):
        post_data = {
            'username': '',
            'email': 'john.m.doe@gmail.com',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field may not be blank.')

    def test_cannot_signup_for_an_account_with_no_email_address(self):
        post_data = {
            'username': 'johndoe',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field is required.')

    def test_cannot_signup_for_an_account_when_email_address_is_blank(self):
        post_data = {
            'username': 'johndoe',
            'email': '',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field may not be blank.')

    def test_can_sign_up_for_an_account(self):
        post_data = {
            'username': 'johndoe',
            'email': 'john.m.doe@gmail.com',
            'password': 'secret_123'
        }

        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # confirm account info is returned
        response_user_data = response.data['user']
        self.assertEqual(response_user_data['username'], post_data['username'])
        self.assertEqual(response_user_data['email'], post_data['email'])

        # confirm a token with a value is returned
        self.assertNotEqual(response.data['token'], '')

        # confirm we have stored new accout in DB
        new_account = Account.objects.get(username=post_data['username'])
        self.assertEqual(new_account.username, post_data['username'])
        self.assertEqual(new_account.email, post_data['email'])


class LoginTest(APITestCase):

    def setUp(self):
        self.account_password = 'top_secret'
        self.account = Account.objects.create_user(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='john.m.doe@gmail.com',
            password=self.account_password
        )

    def test_cannot_login_without_username_and_password(self):
        post_data = {}

        response = self.client.post(reverse('login'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field is required.')
        self.assertEqual(response.data['password'][0], 'This field is required.')

    def test_cannot_login_without_username(self):
        post_data = {
            'password': self.account_password
        }

        response = self.client.post(reverse('login'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field is required.')

    def test_cannot_login_with_empty_username(self):
        post_data = {
            'username': '',
            'password': self.account_password
        }

        response = self.client.post(reverse('login'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field may not be blank.')

    def test_cannot_login_without_password(self):
        post_data = {
            'username': self.account.username,
        }

        response = self.client.post(reverse('login'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], 'This field is required.')

    def test_cannot_login_with_empty_password(self):
        post_data = {
            'username': self.account.username,
            'password': ''
        }

        response = self.client.post(reverse('login'), post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], 'This field may not be blank.')

    def test_can_log_in(self):
        post_data = {
            'username': self.account.username,
            'password': self.account_password
        }

        response = self.client.post(reverse('login'), post_data)

        self.assertContains(response, 'token')
        self.assertNotEqual(response.data['token'], '')


class LogoutTest(APITestCase):
    pass
