from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from .test_links_base import LinkTestMixin


class AccessLinksTest(APITestCase, LinkTestMixin):
    def test_cannot_access_link_information_when_not_authenticated(self):
        login_redirect_url = reverse_lazy('account_login') + '?next=' + reverse_lazy('link-create')

        response = self.client.get(reverse_lazy('link-create'))

        self.assertRedirects(response, login_redirect_url, status_code=302, target_status_code=200)


    def test_can_access_link_information_when_authenticated(self):
        self.authenticate_account()

        response = self.client.get(reverse_lazy('link-create'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Add Link')
        self.assertContains(response, 'Create Link')

    def test_cannot_create_link_when_not_authenticated(self):
        login_redirect_url = reverse_lazy('account_login') + '?next=' + reverse_lazy('link-create')

        response = self.client.post(reverse_lazy('link-create'), data={
            'url': 'https://www.twitter.com/johndoe123',
            'title': 'Twitter'
        })

        self.assertRedirects(response, login_redirect_url, status_code=302, target_status_code=200)

    def test_cannot_create_link_with_invalid_data(self):
        self.authenticate_account()

        response = self.client.post(reverse_lazy('link-create'), data={
            'url': 'invalid_url',
            'title': ''
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(response, 'This field is required.', count=1)
        self.assertContains(response, 'Enter a valid URL.', count=1)