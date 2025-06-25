from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from .test_links_base import LinkTestMixin


class LinksIndexTest(APITestCase, LinkTestMixin):
    def test_cannot_access_link_index_page_when_not_authenticated(self):
        login_redirect_url = reverse_lazy('account_login') + '?next=' + reverse_lazy('link-index')
        response = self.client.get(reverse_lazy('link-index'))

        self.assertRedirects(response, login_redirect_url, status_code=302, target_status_code=200)

    def test_can_access_link_index_page_when_authenticated(self):
        login_redirect_url = reverse_lazy('account_login') + '?next=' + reverse_lazy('link-index')
        response = self.client.get(reverse_lazy('link-index'))

        self.assertRedirects(response, login_redirect_url, status_code=302, target_status_code=200)

    def test_cannot_access_link_index_page_with_invalid_profile(self):
        self.authenticate_account()
        response = self.client.get(reverse_lazy('link-index'))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertContains(response, 'Profile does not exist.', status_code=404)
