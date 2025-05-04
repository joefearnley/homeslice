from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from .test_links_base import LinkTestMixin


class AccessLinksTest(APITestCase, LinkTestMixin):
    def test_cannot_access_link_information_when_not_authenticated(self):
        login_redirect_url = reverse_lazy('account_login') + '?next=' + reverse_lazy('link-create')

        response = self.client.get(reverse_lazy('link-create'))

        self.assertRedirects(response, login_redirect_url, status_code=302, target_status_code=200)
