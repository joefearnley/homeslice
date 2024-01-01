from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class HomepageTest(TestCase):
    def test_homepage_renders(self):
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Homeslice')
