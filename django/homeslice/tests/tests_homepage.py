from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from accounts.models import Account


class HomepageTest(TestCase):
    def test_homepage_renders(self):
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Homeslice')

    def test_authenticated_users_are_redirected_to_dashboard(self):
        username = 'johndoe'
        email = 'john.m.doe@gmail.com'
        password = 'top_secret'

        self.account = Account.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.client.login(username=username, password=password)

        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('dashboard'), status_code=302, target_status_code=200)
