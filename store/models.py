import uuid

from django.db import models


# Create your models here.
class Store(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    owner_id = models.UUIDField()
    name = models.TextField()
    phone_number = models.TextField(
        unique=True,
    )
    is_active = models.BooleanField(default=False)
    priority = models.BigIntegerField(default=10)
    image_url = models.TextField()
    description = models.TextField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    total_visitor = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(blank=True)
    created_by = models.UUIDField(blank=True)
    updated_by = models.UUIDField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "store_models"
