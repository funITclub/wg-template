from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_index_is_shown(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'fun IT club')
