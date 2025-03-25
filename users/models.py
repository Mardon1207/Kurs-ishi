from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('renter', 'Ijarachi'),
        ('owner', 'Ijara Beruvchi'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='renter')  # ✅ Default qo‘shildi
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)  # Viloyat
    district = models.CharField(max_length=100, blank=True, null=True)  # Tuman
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # 📌 Foydalanuvchi email orqali login qila olishi uchun
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username
