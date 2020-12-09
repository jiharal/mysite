import uuid

from django.db import models


# Create your models here.
class Address(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, editable=False,)
    user_id = models.UUIDField()
    user_type = models.CharField(default="store", max_length=60)
    shipping_service = models.CharField(default="raja_ongkir", max_length=60)
    receiver_name = models.CharField(max_length=60)
    address = models.TextField()
    address_1 = models.TextField()
    city_id = models.CharField(max_length=5)
    city = models.CharField(max_length=60)
    subdistrict_id = models.CharField(max_length=5)
    subdistrict = models.CharField(max_length=100)
    province_id = models.CharField(max_length=5)
    province = models.CharField(max_length=100)
    country_id = models.CharField(default="ID", max_length=5)
    country = models.CharField(default="Indonesia", max_length=60)
    type_address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    postal_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(blank=True)
    created_by = models.UUIDField(blank=True)
    updated_by = models.UUIDField(blank=True)

    def __str__(self):
        return self.receiver_name

    class Meta:
        db_table = "address_models"
