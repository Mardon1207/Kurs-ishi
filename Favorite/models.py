from django.db import models
from django.conf import settings
from listings.models import Listing  # ✅ E’lon modelini import qilamiz

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ Foydalanuvchi
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)  # ✅ E’lon
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Qo‘shilgan vaqt

    class Meta:
        unique_together = ('user', 'listing')  # ✅ Har bir e’lon faqat bir marta saqlansin

    def __str__(self):
        return f"{self.user.username} - {self.listing.title}"
