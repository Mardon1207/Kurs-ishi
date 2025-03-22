from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Favorite
from .serializers import FavoriteSerializer
from listings.models import Listing  # ✅ E’lon modelini chaqiramiz

# ✅ Sevimlilarga qo‘shish
class FavoriteCreateView(generics.CreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Faqat login bo‘lgan foydalanuvchilar

    def perform_create(self, serializer):
        listing_id = self.request.data.get("listing")
        listing = Listing.objects.get(id=listing_id)  # ✅ E’lonni olish

        # ✅ Foydalanuvchi allaqachon shu e’lonni saqlaganmi?
        if Favorite.objects.filter(user=self.request.user, listing=listing).exists():
            raise ValidationError("Bu e'lon allaqachon sevimlilarga qo‘shilgan!")

        serializer.save(user=self.request.user, listing=listing)

# ✅ Foydalanuvchining sevimlilari
class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Faqat login bo‘lgan foydalanuvchilar

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)  # ✅ Faqat o‘z sevimlilari

# ✅ Sevimlilardan o‘chirish
class FavoriteDeleteView(generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Faqat login bo‘lgan foydalanuvchilar

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)  # ✅ Faqat o‘z sevimlilari o‘chira oladi
