from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import SignUpForm

class SignUpTest(TestCase):

    def test_signup_page_renders(self):
        response = self.client.get('/signup/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Create an Account')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Already have an account?')
        self.assertContains(response, 'Sign up')

    def test_signup_redirects_after_saved(self):
        form_data = {
            'email': 'john.doe123@gmail.com',
            'password1': 'topsecret123',
            'password2': 'topsecret123',
        }

        response = self.client.post('/signup/', data=form_data)
        self.assertRedirects(response, '/bookmarks/', 302)

class SignUpFormTest(TestCase):
    def test_form_does_not_validate_with_empty_data(self):
        form_data = {
            'email': '',
            'password1': '',
            'password2': '',
        }

        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_does_not_validate_with_no_email(self):
        form_data = {
            'email': '',
            'password1': 'topsecret123',
            'password2': 'topsecret123',
        }

        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_does_not_validate_with_no_password(self):
        form_data = {
            'email': 'john.doe123@gmail.com',
            'password1': '',
            'password2': '',
        }

        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_does_not_validate_with_no_password_confirmation(self):
        form_data = {
            'email': 'john.doe123@gmail.com',
            'password1': 'topsecret123',
            'password2': '',
        }

        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_does_not_validate_with_no_password_confirmation_match(self):
        form_data = {
            'email': 'john.doe123@gmail.com',
            'password1': 'topsecret123',
            'password2': 'topsecret1234',
        }

        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_validates(self):
        form_data = {
            'email': 'john.doe123@gmail.com',
            'password1': 'topsecret1234',
            'password2': 'topsecret1234',
        }

        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())


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
        form_data = {
            'email': '',
            'password': 'secret123'
        }

        response = self.client.post('/login/', form_data)

        self.assertEqual(response.status_code, 405)

    def test_user_can_login(self):
        pass
        user = User.objects.create_user(
            email='joe124@gmail.com',
            password='top_secret',
            password_confirmation="top_secret"
        )


class LogoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='user1',
            email='user1_123@gmail.com',
            password='top_secret123'
        )

    def test_user_logs_out(self):
        self.client.login(email=self.user.email, password=self.user.password)
        self.assertTrue(self.user.is_authenticated)

        response = self.client.get('/logout/')
        self.assertRedirects(response, '/', 302)
