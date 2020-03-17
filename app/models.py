import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.contrib.gis.db import  models as geo_models


# Create your models here.
class Toilet(models.Model):
    toilet_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    location = geo_models.PointField(srid=4326)
    image_1 = models.ImageField(upload_to='img/', null=True)
    image_2 = models.ImageField(upload_to='img/', null=True)
    image_3 = models.ImageField(upload_to='img/', null=True)
    description = models.CharField(max_length=200, null=True)
    accesibility = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField('Created time', auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.description
