from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Listing(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)  # ✅ Qo‘shildi
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Kategoriya
    latitude = models.FloatField(null=True, blank=True)  # Kenglik (GPS)
    longitude = models.FloatField(null=True, blank=True)  # Uzunlik (GPS)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='listing_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    

