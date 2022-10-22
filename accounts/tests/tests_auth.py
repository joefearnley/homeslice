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
            'email': 'joe123@gmail.com',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field is required.')

    def test_cannot_signup_for_an_account_when_username_is_blank(self):
        post_data = {
            'username': '',
            'email': 'joe123@gmail.com',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'This field may not be blank.')

    def test_cannot_signup_for_an_account_with_no_email_address(self):
        post_data = {
            'username': 'joe123',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field is required.')

    def test_cannot_signup_for_an_account_when_email_address_is_blank(self):
        post_data = {
            'username': 'joe123',
            'email': '',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field may not be blank.')

    def test_can_sign_up_for_an_account(self):
        post_data = {
            'username': 'joe123',
            'email': '',
            'password': 'secret_123'
        }
        response = self.client.post('/api/v1/signup/', post_data)

        print(response)

        # self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(response.data['email'][0], 'This field may not be blank.')

class LoginTest(APITestCase):
    pass


class LogoutTest(APITestCase):
    pass


    # def test_can_update_account_information(self):
    #     pass

    # update name
    #  validation
    #       not empty

    # update email address
    #  validation
    #       not empty
    #       valid email
    #       email not already i user

    # update username
    #  validation
    #       not empty
    #       not already in use

    # update password
    #  validation
    #    not empty
    #    at least 8 characters
    #    confirmation matches
