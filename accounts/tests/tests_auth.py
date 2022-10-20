from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import User
from accounts.models import Account


class SignupTest(APITestCase):
    def test_cannot_signup_for_an_account_with_no_data(self):
        response = self.client.post('/api/v1/accounts/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

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
