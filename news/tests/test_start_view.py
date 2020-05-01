from django.test import TestCase, Client


class StartViewTestCase(TestCase):
    def test_get(self):
        client = Client()
        url = '/hello/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
