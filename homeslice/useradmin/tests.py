from django.test import TestCase, Client
from django.contrib.auth.models import User


class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_page_renders(self):
        response = self.client.get('/login/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Forgot your password?')
        self.assertContains(response, 'Login')

    def test_login_form_requires_email(self):
        pass
        # form_data = {
        #     'email': '',
        #     'password': 'secret123'
        # }

        # response = self.client.post('/login/', form_data)

        # self.assertEqual(response.status_code, 405)

    def test_user_can_login(self):
        pass
        # user = User.objects.create_user(
        #     name='Joe Fearnley',
        #     email='joe124@gmail.com',
        #     password='top_secret',
        #     password_confirmation="top_secret"
        # )



class RegisterTest(TestCase):

    def test_registration_page_renders(self):
        response = self.client.get('/register/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'register.html')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Confirm Password')
        self.assertContains(response, 'Already registered?')
        self.assertContains(response, 'Register')
