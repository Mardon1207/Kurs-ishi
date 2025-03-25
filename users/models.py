from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('renter', 'Ijarachi'),
        ('owner', 'Ijara Beruvchi'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='renter')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'  # 📌 Login uchun faqat username ishlatiladi
    REQUIRED_FIELDS = ['email']  # ✅ Ro‘yxatdan o‘tishda email majburiy bo‘ladi

    def __str__(self):
        return self.username  # ✅ Endi username orqali login bo‘ladi
