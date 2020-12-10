"""
This module is used to test store
"""
import uuid
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse, resolve

from .models import Store
# Create your tests here.

"""
StoreTestCase is used to test
"""


class StoreTestCase(TestCase):
    def setUp(self):
        Store.objects.create(
            owner_id=uuid.uuid4(),
            name="kancio shop",
            phone_number="089020394003",
            is_active=True,
            priority=1,
            image_url="img.png",
            description="kancio store",
            latitude=10,
            longitude=20,
            total_visitor=100,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            created_by=uuid.uuid4(),
            updated_by=uuid.uuid4(),
        )

    def test_get(self):
        mdl = Store.objects.get(name="kancio shop")
        print(mdl.name)


class StoreClientTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list(self):
        store_list = reverse('store:list')
        uri = resolve(store_list)
        data = self.client.get(uri.route)
        print(data)