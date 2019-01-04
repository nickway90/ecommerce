from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class AddressType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class UserAddress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addresses")
    type = models.ForeignKey(
        AddressType, on_delete=models.SET_NULL, null=True, related_name="addresses")
    street_1 = models.CharField(max_length=300)
    street_2 = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
