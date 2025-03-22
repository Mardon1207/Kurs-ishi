from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('renter', 'Ijarachi'),
        ('owner', 'Ijara Beruvchi'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='renter')  # ✅ Default qo‘shildi
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
