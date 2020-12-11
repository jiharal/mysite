from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class CommentsClientTest(TestCase):
    databases = {'mongo'}
    def test_list(self):
        url = reverse('comments:list')
        data = self.client.get(url)
        print(data.json())
        self.assertEqual(data.status_code, status.HTTP_200_OK)
