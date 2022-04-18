from django.test import TestCase
from django.urls import reverse

class RestaurantViewTestCase(TestCase):
    def test_view_output(self):
        url = "/hello-world/"
        response = self.client.get(url)
        self.assertIn("Hello World!", response.context['msg'])
        self.assertContains(response, "Hello World!")
        self.assertEqual(response.status_code, 200)
