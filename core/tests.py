from django.test import TestCase
from django.urls import reverse

from .views import IndexView


class IndexViewTests(TestCase):
    def test_index_is_shown(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'fun IT club')

    def test_index_is_public(self):
        """本番は既定でログイン必須。誰でも見せるページは外してあること。"""
        self.assertIs(IndexView.dispatch.login_required, False)
