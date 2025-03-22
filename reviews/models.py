from django.db import models
from django.conf import settings
from listings.models import Listing  # ✅ Listings modelini chaqiramiz

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")  # E’lon
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Sharh egasi
    rating = models.IntegerField(default=5)  # Reyting (1 dan 5 gacha)
    comment = models.TextField()  # Sharh matni
    created_at = models.DateTimeField(auto_now_add=True)  # Sharh vaqti

    def __str__(self):
        return f"{self.user.username} - {self.listing.title} ({self.rating})"
