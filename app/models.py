import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Toilet(models.Model):
    toilet_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('Costumer', on_delete=models.CASCADE)
    provider_id = models.ForeignKey('Provider', on_delete=models.CASCADE)
    ubication = models.CharField(max_length=200)
    image = models.FilePathField(path=None, match=None, recursive=False, null=True)
    description = models.CharField(max_length=200)
    accesibility = models.BooleanField(default=False)
    created_at = models.DateTimeField('Created time', auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True)

class Provider(models.Model):
    provider_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False,)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50)
    create_at = models.DateTimeField('Created time', auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True)

class Costumer(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField('Created time', auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name